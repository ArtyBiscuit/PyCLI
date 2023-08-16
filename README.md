# Braillengine

Engine to render images with the braille characters (0x2800-0x28FF)

By [ArtyBiscuit](https://github.com/ArtyBiscuit)
and [Pixailz](https://github.com/Pixailz)

## TODO

1. print BrailleVid
   1. rework the parsing of `.bvi` file in [file2BrailleVid](./utils/braillEngine.py)
1. add parsing

## The braille char

The braille character are a character that display dot in a rectangle of 2x4.
it contain all the combination of those dot

The braille char is starting at the index 0x2800 and end at 0x28FF in the
unicode table.

With the two upper rules, we have discovered that we can map the dot in a `char`
sized number value by setting certain bit.
like so:

```
76543210 // char bytes

03
14
25
67

so

10010011 = ⢓
11111110 = ⡿
```

etc...

## HOWTO

### Dependency

Checkout [requirements.txt](./requirements.txt) to see all the dependency

To easilly install all those, run `python3 -m pip install -r requirements.txt`
