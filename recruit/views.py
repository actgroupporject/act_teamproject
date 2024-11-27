from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from .forms import RecruitForm
from .models import Recruit


def recruit_list(request):  # 공고 목록 조회
    recruits = Recruit.objects.all()
    return render(request, "recruit/recruit_list.html", {"recruits": recruits})


def recruit_detail(request, pk):  # 공고 상세 정보 조회
    recruit = get_object_or_404(Recruit, pk=pk)
    return render(request, "recruit/recruit_detail.html", {"recruit": recruit})


@login_required  # 로그인해야 공고 생성, 수정 가능
def recruit_create_or_update(request, pk=None):
    recruit = None if pk is None else get_object_or_404(Recruit, pk=pk)
    if request.method == "POST":
        form = RecruitForm(request.POST, instance=recruit)
        if form.is_valid():
            recruit = form.save()
            messages.success(request, "채용 공고가 성공적으로 저장되었습니다.")
            return redirect("recruit:detail", pk=recruit.pk)
    else:
        form = RecruitForm(instance=recruit)
    return render(request, "recruit/recruit_form.html", {"form": form})


@method_decorator(login_required, name="dispatch")  # 로그인 해야 삭제 가능
class RecruitDeleteView(DeleteView):
    model = Recruit
    success_url = reverse_lazy("recruit:list")
    template_name = "recruit/recruit_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "채용 공고가 성공적으로 삭제되었습니다.")
        return super().delete(request, *args, **kwargs)


recruit_create = login_required(recruit_create_or_update)
recruit_update = login_required(recruit_create_or_update)
recruit_delete = RecruitDeleteView.as_view()
