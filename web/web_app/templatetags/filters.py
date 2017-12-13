from django import template

register = template.Library()


@register.filter(name='material_field')
def material_field_transform(value):
    field = value.field.widget.__class__.__name__
    if field == 'TextInput' or field == 'PasswordInput':
        add_class = 'mdl-textfield__input'
    elif field == 'CheckboxInput':
        add_class = 'mdl-switch__input'
    else:
        return field
    return value.as_widget(attrs={'class': add_class})


@register.filter(name='material_checkbox')
def material_checkbox_transform(value):
    return value.as_widget(attrs={'class': 'mdl-checkbox__input'})
