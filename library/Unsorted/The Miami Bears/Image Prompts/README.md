# Image Prompts: The Miami Bears

Work queue for Ledger. One file per image.

## For each `.md` file in this folder (skip this README)

1. Read the frontmatter. Only process files with `status: pending`.
2. Generate one image from the **Prompt** section, using the **Negative Prompt** section as the negative prompt.
3. Use the `aspect_ratio` in the frontmatter (all are 1:1 square). PNG format.
4. Save the image to the exact path in `output`. Never overwrite an existing image; if the path is taken, add ` (alt 2)`, ` (alt 3)`, and so on before `.png`.
5. Change that file's `status` to `done` and add a line `image: <path you saved to>`.
6. Commit with a message like `Miami Bears: Marcus portrait`.

## The queue

| File | Character | Saves to |
| --- | --- | --- |
| Marcus.md | Marcus Delgado | Marcus (Miami Bears)/Marcus (Miami Bears).png |
| Javi.md | Javier "Javi" Reyes | Javi (Miami Bears)/Javi (Miami Bears).png |
| Leo.md | Leo Callaway | Leo (Miami Bears)/Leo (Miami Bears).png |
| Zion.md | Zion Marsh | Zion (Miami Bears)/Zion (Miami Bears).png |
| The Miami Bears (group).md | All four together | The Miami Bears/The Miami Bears (alt 1).png (the folder already has a group image) |

## Look-consistency notes

- Every Bear is bearded and hairy-chested. Keep them visibly different: Marcus biggest with a black beard, Javi tanned with a trimmed dark beard and dimples, Leo strawberry-blonde with a copper beard and blue eyes, Zion auburn and freckled with green eyes and a gold cross.
- All characters are adults. Portraits are SFW (avatar-safe).
