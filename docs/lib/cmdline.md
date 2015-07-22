cmdline.py
=======

### `email`
+ desc: validator of email address
+ params: string, type: str
+ returns: string
+ exceptions: ValueError

### `date`
+ desc: validator of date strings
+ params: date\_string, type: str
+ returns: time.struct\_time
+ returns: None

### `cmd_parser`
+ desc: command parameters parser function
+ params: none
+ returns: tuple of (argparse.Namespace, list)
+ exceptions: SystemExit, Exception