from voluptuous import Schema, PREVENT_EXTRA, Required, Optional


class Login:
    successful = Schema(
        {
            "token": str,
        },
        required=True,
        extra=PREVENT_EXTRA,
    )

    unsuccessful = Schema(
        {
            "error": str,
        },
        required=True,
        extra=PREVENT_EXTRA,
    )


class User:
    created = Schema(
        {Required("name"): str, "job": str, "id": str, Optional("createdAt"): str},
        required=True,
        extra=PREVENT_EXTRA,
    )

    data = Schema(
        {
            Required("data"): {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str,
            },
            Optional("support"): {"url": str, "text": str},
        },
        required=True,
        extra=PREVENT_EXTRA,
    )


class Resource:
    single = Schema(
        {
            "data": {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str,
            },
            Optional("support"): {"url": str, "text": str},
        },
        required=True,
        extra=PREVENT_EXTRA,
    )

    list = Schema(
        {
            "page": int,
            "per_page": int,
            "total": int,
            "total_pages": int,
            Required("data"): [
                {
                    "id": int,
                    "name": str,
                    "year": int,
                    "color": str,
                    "pantone_value": str,
                }
            ],
            Optional("support"): {"url": str, "text": str},
        },
        required=True,
        extra=PREVENT_EXTRA,
    )
