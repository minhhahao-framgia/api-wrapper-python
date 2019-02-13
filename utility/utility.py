
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 25

API_CONCEPT = 'https://{workspace_api_domain}/{api_type}/{api_version}/{api_sub_url}'


def validate_password(password):
    if len(password) < PASSWORD_MIN_LENGTH or len(password) > PASSWORD_MAX_LENGTH:
        raise ValidationError('Length of password is invalid')

    if ' ' in password:
        raise ValidationError('Not contain any whitespace')

    return True


def set_url(workspace_api_domain, api_type, api_version, api_sub_url):
    """

    :param workspace_api_domain:
    :param api_type:
    :param api_version:
    :param api_sub_url:
    :return:
    """
    return API_CONCEPT.format(
            workspace_api_domain=workspace_api_domain,
            api_type=api_type,
            api_version=api_version,
            api_sub_url=api_sub_url
        )
