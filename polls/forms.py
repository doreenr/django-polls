from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Add an anonymous comment…"}),
        max_length=1000,
    )