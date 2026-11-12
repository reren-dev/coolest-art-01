# The Last Pine

**The Last Pine** is a striking digital artwork rendered in a traditional Japanese ukiyo-e woodblock print style. 

## Artwork Description

At the center of the composition stands a single, defiant charred pine tree engulfed in a ferocious wave of fire. Above, a solitary white crane flees frantically against a stark, blood-red sun. Below, the ancient forest is reduced to smoking, blackened stumps, while on a distant hill, a luxurious golden palace glows untouched and indifferent to the devastation. 

## Conceptual Message

The artwork serves as a powerful social and environmental commentary, illustrating how nature and ordinary life bear the catastrophic costs of the ruling elite's greed and exploitation—symbolized here by destructive deforestation, forest fires (*karhutla*), and systemic neglect.

## Judging notes

The piece is built to read at small size (one central tree, one red sun, one golden palace) and carries no text.

## Implementation

The entry program `main.py` is written in Python 3 using only the standard library. It locates the bundled `entry.png` artwork (a 1024x1024 JPEG image weighing 481,906 bytes, well under the 1 MiB competition limit) and deterministically copies it to the output directory specified by the `MAKEFUN_OUTPUT_DIR` environment variable, ensuring byte-identical reproduction across runs.
