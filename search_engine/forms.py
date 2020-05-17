from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit
from django import forms


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
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    discipline = forms.MultipleChoiceField(
        choices=(
            ("Desert Wind", "Desert Wind"),
            ("Devoted Spirit", "Devoted Spirit"),
            ("Diamond Mind", "Diamond Mind"),
            ("Iron Heart", "Iron Heart"),
            ("Setting Sun", "Setting Sun"),
            ("Shadow Hand", "Shadow Hand"),
            ("Stone Dragon", "Stone Dragon"),
            ("Tiger Claw", "Tiger Claw"),
            ("White Raven", "White Raven"),
        ),
        widget=forms.CheckboxSelectMultiple,
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
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    type = forms.MultipleChoiceField(
        choices=(
            ("Boost", "Boost"),
            ("Counter", "Counter"),
            ("Stance", "Stance"),
            ("Strike", "Strike"),
            ("Other", "Other"),
        ),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    helper = FormHelper()
    helper.form_id = "main-form"
    helper.layout = Layout(
        Div(
            Field("maneuver_name", placeholder="Exact partial maneuver name."),
            Div(
                Div(Field("level"), css_class="col-md-3"),
                Div(Field("discipline"), css_class="col-md-3"),
                Div(Field("requirements"), css_class="col-md-3"),
                Div(Field("type"), css_class="col-md-3"),
                css_class="row",
            ),
        )
    )
    helper.add_input(Submit("submit", "Search"))
