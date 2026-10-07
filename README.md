# WordPress Library

The WordPress Library is a home for books about the history and development of WordPress. Each book is a volume in the *Milestones* series.

## Volumes

### [Vol. 1 — Milestones: The Story of WordPress](milestones-vol-1/)

The origins of WordPress and its first decade. [Read the book](milestones-vol-1/) · Formats: [EPUB](milestones-vol-1/Formats/Milestones-The-Story-of-WordPress.epub) · [PDF](milestones-vol-1/Formats/Milestones-The-Story-of-WordPress.pdf) · [MOBI](milestones-vol-1/Formats/Milestones-The-Story-of-WordPress.mobi)

### [Vol. 2 — Building Blocks: The Evolution of WordPress](milestones-vol-2/)

WordPress' second decade — the Gutenberg project, the global pandemic, and a look at where the project is headed. [Read the book](milestones-vol-2/) · Formats: [EPUB](milestones-vol-2/Formats/Building%20Blocks%20The%20Evolution%20of%20WordPress%20%282page%29.epub) · [PDF](milestones-vol-2/Formats/Building_Blocks_The_Evolution_of_WordPress.pdf) · [MOBI](milestones-vol-2/Formats/Building%20Blocks%20The%20Evolution%20of%20WordPress.mobi)

## How wordpress.org/book updates

[wordpress.org/book](https://wordpress.org/book/) shows the chapters from this repo. [`manifest.json`](manifest.json) lists every chapter file and the post it fills on the site, and the site re-imports each chapter after it changes on `trunk`. Edit the Markdown here rather than on the site, since the next import replaces edits made there.

- The post title comes from `title` in the manifest. The book title and chapter heading at the top of each file are left off the web page because the site already shows them.
- Footnotes use standard Markdown: `[^1]` in the text and `[^1]: The note.` at the end of the chapter.
- A new chapter needs a post on the site first, then a manifest entry with that post's slug.
- `python3 bin/check-manifest.py` checks the manifest and footnotes. It also runs on every pull request.

## Feedback

The following feedback is particularly valuable:
- *Factual errors*: notes about factual errors are welcome. All suggestions for changes should be evidenced with links that back up any claims. Any facts that cannot be corroborated will not be included.
- *Clarity*: any paragraphs or sections that you feel are not clear. This would be of particular help in sections that are technical in nature.
- *Omissions*: anything that you feel has been omitted or not sufficiently covered. Suggestions about omissions should be accompanied with information about why it should be included, and backed up with evidence as to their importance.
- *Images*: if you have any images that you feel would complement the text, we'd love to have them.

All feedback should be opened as [issues](https://github.com/WordPress/library/issues) in the tracker.

## License

Both books are dual-licensed under [GPLv2](license-gpl.txt) and [Creative Commons Sharealike 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Just like WordPress, you are free to read, share, distribute, and modify the content however you want, passing on those freedoms to everyone else.
