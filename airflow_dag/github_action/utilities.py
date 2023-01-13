def authenticate_to_github(func):
    def wrapper(*args, **kwargs):
        wrapper.OWNER = "machkouroke"
        wrapper.REPO = "LOPProno"

        wrapper.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer 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',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        return func(*args, **kwargs)

    return wrapper
