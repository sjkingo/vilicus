This app provides Android push notifications via the [Pushover](https://pushover.net/) service.

You need to add the `NOTIFY_PUSHOVER_API_TOKEN` configuration option to `local_settings.py` for
this to work, and register users in the `PushoverUser` model.

Make sure you run `pip install -r notify_pushover/requirements.txt` to add the dependencies.
