from django import forms

from .models import Recruit


# Recruit모델 기반 ModelForm
class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ["company_name", "title", "description", "closing_date"]
        # closing_date필드에 대해 datetime-local 타입의 위젯 추가
        widgets = {
            "closing_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    # clean_closing_date에서 마감일의 유효성 추가로 검사
    def clean_closing_date(self):
        closing_date = self.cleaned_data.get("closing_date")
        from django.utils import timezone

        if closing_date and closing_date <= timezone.now():
            raise forms.ValidationError("마감일은 현재 시간보다 미래여야 합니다.")
        return closing_date
