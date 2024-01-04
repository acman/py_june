from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "title",
            "content",
            Submit("submit", "Create Post", css_class="btn waves-effect waves-light"),
        )
        self.field_order = ["title", "content"]
