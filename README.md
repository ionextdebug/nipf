# NOSTR Facilities (nipf)

Python source code to download `.zip` compressed folders with facilities created to NOSTR community.

# HOW TO USE

Clone this repository and execute the command:
```./nipf <org>/<repository> <foldername>```

`<org>` is the name of the organization/user who owns the repository on Github
`<repository>` is the name of the repository that contains the compressed facility 
`<foldername>` is the name of the `.zip` file, without the extension `.zip`

For example:
```./nipf nextdebug/nipf-example pptx```

[Click here to see the repository](https://github.com/nextdebug/nipf-example)

## Where are the facilities?

The facilities are download in the folder `nostr_facilities`, then you can import in your projects.

# LINUX

Set the `nipf` as global command:
```cp nipf /usr/local/bin```

Then you can run:
```nipf <org>/<repository> <foldername>```

For example:
```nipf nextdebug/nipf-example pptx```

# HOW TO COMPILE

```python -m PyInstaller nipf --onefile```