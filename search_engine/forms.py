from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions


class SearchForm(forms.Form):
    maneuver_name = forms.CharField(label="Name", required=False)

    level = forms.MultipleChoiceField(
        choices=(
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
        ),
        # widget = forms.CheckboxSelectMultiple,
        required=False,
        # help_text="Hold down ctrl to deselect or multi-select."
    )

    discipline = forms.MultipleChoiceField(
        choices=(
            ("White Raven", "White Raven"),
            ("Tiger Claw", "Tiger Claw"),
            ("Stone Dragon", "Stone Dragon"),
            ("Shadow Hand", "Shadow Hand"),
            ("Setting Sun", "Setting Sun"),
            ("Iron Heart", "Iron Heart"),
            ("Diamond Mind", "Diamond Mind"),
            ("Devoted Spirit", "Devoted Spirit"),
            ("Desert Wind", "Desert Wind"),
        ),
        # widget = forms.CheckboxSelectMultiple,
        required=False,
    )

    requirements = forms.MultipleChoiceField(
        choices=(
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
        ),
        # widget = forms.CheckboxSelectMultiple,
        required=False,
    )

    helper = FormHelper()
    # helper.form_class = "form-horizontal"
    helper.layout = Layout(
        Field("maneuver_name", placeholder="Exact partial maneuver name."),
        Field("level"),
        Field("discipline"),
        Field("requirements"),
        FormActions(
            Submit("search", "Search", css_class="btn btn-default"),
        )
    )
    helper.form_action = "/"