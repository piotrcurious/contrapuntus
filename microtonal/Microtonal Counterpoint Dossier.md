# Microtonal Counterpoint Dossier

Nov 2, 2026 · @Piotr Curious

Every statement in the lab carries one of five labels (arithmetic, a source's report, a count on a named collection, a model's output, or an open gap), and every number that is a guess is a setting you can change.

## Where things stand

The research record, the lab and the listening page are built and tested; nothing has been put into a new composer yet.

| Piece | State |
| --- | --- |
| Research record | 100 source records behind 44 source reports (K), 50 recalled items marked as not evidence (Q) and 24 gaps (G). 18 records were re-read against their sources: 16 held, 2 were corrected. The 13 records added in the second round were each read once. |
| Lab | 14 modules (the newest, 10-corpus, holds the counting rules) and 125 registered settings. 97 are assumptions, 16 sit inside a range a source gives, 4 are measured, 2 follow from other settings, 6 copy what the published composer does. |
| Sketches | 16 small scripts that print tables; each write-up says what the script cannot tell. |
| Tests | 13 suites, 588 checks, all passing. The listening page also passes 86 checks in a real browser. |
| Counts on real music | SymbTr, five music21 collections and the Cantometrics codings, counted by written rules (93 of the checks above). The composer's output at nine divisions is run through the same rules and printed beside them. research/CORPUS.md, generated from small tables. |
| Fix list | Five options and six counts that point at no option, every one marked not built, each option with its default. research/FIXES.md. |
| Listening lab | Published. One sitting is kept: one listener, bluetooth speakers, 2026-11-01. |
| Published composer | Not edited. The lab reads its modules only to check that a frame in the legacy reading gives the same numbers. |
| Not done | Putting any of this into a new composer. The integration plan below lists the steps. |

## What changed after the review of 3 November

You wrote that the first round "collected very little new data on how to fix the composer", did not use "inference from the music itself or from larger projects collecting and comparing musical pieces", and that "even the consonance research across microtonal scales is quite poor". All three were accurate. The second round (4 to 9 November) was done without agents and without touching the published composer. It added:

- **Counts on real music.** SymbTr (2,200 Turkish makam scores in 53-comma notation), the music21 collections (371 Bach chorales, 1,318 Palestrina pieces, 49 Monteverdi, 103 Trecento, 8,514 Essen songs) and the Cantometrics codings of 5,776 songs, counted by written, tested rules, with the composer's own output at nine divisions run through the same rules and printed in the same tables. See "Counts on real music".
- **Literature on consonance across tunings and on the large comparative projects.** Thirteen new records (T-01 to T-05, P-01 to P-04, W-01 to W-04) and nine new entries of what is known (K-36 to K-44), each with what it supports and where it stops. See "Consonance across tunings, and the large projects".
- **A fix list.** Five options (F1 to F5), each with its source, its default (the current behaviour), what the data cannot say and how to check it once built, and six counts that point at no option. Nothing is built. See "Fix list".
- **Two new gaps.** G-29: no measured vertical intervals of microtonal polyphony. G-30: no listener test of chords or counterpoint at 19 or more divisions.

It did not find a symbolic collection of microtonal polyphony. Nothing in the counts ranks the composer against a collection, and nothing in them says that any output sounds better or worse.

## The five kinds of statement

Every line in the lab (code comments, setting notes, audit findings, write-ups) is arithmetic, a source's report, a count on a named collection, a model's output or a gap, and nothing else is allowed to look like a finding.

| Kind | What it is | How to check it | Example |
| --- | --- | --- | --- |
| Arithmetic | Follows from definitions. No source, no model. | By hand. | A just fifth (3/2) is 701.955 cents. In 53 divisions the nearest step is step 31, at 701.89 cents. |
| A source reports | A number or statement from a paper or book that was fetched and quoted, with its strength and conditions. "Recalled" means from memory: not evidence. | Open the cited record and read the quote. | Practised listeners tell two pure tones apart at about 0.5% at 200 Hz (K-03). |
| A count on a collection | A count, or a per-piece distribution (smallest, quartiles, largest), of a quantity that a written rule defines, on a named collection and version, with n. The same rule is run on the composer's output and printed beside it. It says what the collection contains and nothing more. | Re-run the extraction (research/corpora/MANIFEST.md). A test rebuilds research/CORPUS.md from the small tables and compares it with the file. | In SymbTr 2.4.3 (2,200 scores), 0.004 of the gaps between neighbouring core pitch classes of a piece are under 45 cents (15,115 gaps). |
| A model computes | The lab's own calculation: numbers from sources plus assumed settings, run on a case. | Re-run it, change a setting, watch the number move. | The roughness of a triad at 131 Hz under the ERB width law. It says what the calculation gives, not what listeners hear. |
| A gap | Not known, or an inference the lab chose not to make. | The ledger says what would settle it. | G-28: no counterpoint corpus inside the Moroccan or Tuvan traditions was found. |

A mixed statement takes the kind of its least certain part. Arithmetic set against a source's number is a source statement; anything that passes through a model is a model statement.

Statistics are allowed in four uses only: a source's own result quoted with its conditions; how far a model's answer moves when its own assumed settings are varied, reported as counts of runs; checks that two versions of the code return the same numbers; and counts and per-piece distributions of a quantity that a written rule defines, on a named collection, with the same rule run on the composer's output beside them. Refused:

- counting how often a model matches a recalled rule
- correlating the lab's own models with each other
- averages, medians or shares of a measure the lab invented
- adjusting settings until a recalled order appears

After the review of 30 October every sketch and note that did one of these was rewritten or removed. `research/CLAIMS.md` lists each change. The counts of the second round are of categories that a written rule defines (a move of at least 250 cents is a leap), carry the collection's name and version, and are not correlated, ranked or tested; the section "Corpus measurements" of that file says what they may and may not be used for.

## What the sources report

The sources give firm numbers for the ear and for auditory scenes, and only weak, descriptive accounts of the traditions. Strength is the ledger's rating of the records behind an entry, best / weakest. Each entry id leads to `research/LEDGER.md`, where every record has its link and how much of it was read.

### Ear and nerve

| What the sources report | Strength | Entry |
| --- | --- | --- |
| The ear's filter widens with pitch: at moderate levels ERB = 24.7 (4.37 F + 1) Hz, F in kHz. Which law holds in the bass is open (G-10). | weak / weak | K-01 |
| Masking is lopsided. The low side of a masker falls about 27 dB per Bark whatever the level; the high side is shallower and depends on the masker's level. | weak / weak | K-02 |
| Practised listeners tell pure tones apart at about 0.5% at 200 Hz and 0.2% at 1 kHz. Untrained listeners start more than six times worse; training cuts that several-fold (still about four times worse after 2 hours). | moderate / weak | K-03 |
| The cochlea separates the harmonics below about the 6th. Opinions differ for the 6th to the 12th. | moderate / moderate | K-04 |
| A mistuned partial is heard out as a separate tone at about 1% to 3% (17 to 51 cents) for 410 ms tones. The threshold rises 3 to 5 times as the tone shortens from 1610 ms to 50 ms. Four listeners. | moderate / moderate | K-05 |
| Musicians hear out partials better than non-musicians without narrower filters. In cochlear loss, wider filters go with poorer hearing-out. So partial resolution is not only filter width, and training matters. | moderate / moderate | K-06 |
| For pairs of pure tones the dissonance peaks near a quarter of the critical bandwidth and is gone at the full bandwidth. | strong / strong | K-07 |
| Slow fluctuation (strongest near 4 Hz, up to about 20 per second) and roughness (about 20 to 300 per second, peak near 70 Hz) are different sensations, with a gradual boundary near 20 Hz. | weak / weak | K-08 |
| The human cochlea has about 3,500 inner hair cells and about 30,000 auditory-nerve fibres. Cochlear compression can be measured by listening tests and agrees with physiological estimates in normal listeners. | moderate / weak | K-10 |
| Phase locking in the auditory nerve is strongest up to about 1 to 3 kHz in cat and guinea pig and falls to the noise floor near 4 kHz. For humans, specialists put the upper limit of its use anywhere between 1.5 and 10 kHz. There is no consensus. | strong / strong | K-11 |
| Ten musicians put the upper limit of musical pitch at about 4.7 kHz on average (individual means spread by about three semitones). Whether pitch needs phase locking at all is contested. | moderate / weak | K-12, K-13 |
| Brainstem responses of non-musicians rank consonant twelve-tone intervals above dissonant ones. Across more than 250 listeners only the liking of harmonic spectra tracked the liking of consonant chords, not the dislike of beating. Nothing here covers microtonal intervals. | strong / moderate | K-14 |
| Beat perception couples auditory and motor planning regions. This is about rhythm. Vocal motor control of pitch was not searched (G-14). | moderate / moderate | K-15 |

### Auditory scenes, objects and memory

| What the sources report | Strength | Entry |
| --- | --- | --- |
| Accuracy in counting the voices of a texture of one timbre drops sharply from three to four, usually by underestimating. Up to about three simultaneous pure-tone lines can be separated. Mixed timbres are not covered (G-18). | moderate / moderate | K-16 |
| Attention works on one auditory object at a time. What an "object" is has no settled definition or neural basis (G-19). | moderate / unrated | K-17 |
| Working memory holds about four chunks when rehearsal and long-term memory cannot help (three to five by other estimates). | strong / moderate | K-18 |
| Long-term auditory memory is large and lasting: listeners recognise meaningless noise sounds weeks later, and untrained adults keep the pitch of familiar tunes to within a semitone or two. With K-16 to K-18 this is the contrast the scene layer is built on: what can be remembered far exceeds what can be tracked at once. | moderate / weak | K-19 |
| Absolute identification of single pitches stops at about six (2.5 bits). The smallest noticeable change in an interval's size is often of the order of the interval itself in non-musicians. Interval identification is worse in the lowest octave and for short notes. None of this gives a category width in cents. | moderate / moderate | K-20 |
| Mistuning is judged by the beat rates of nearly coinciding harmonics: accepted mistunings narrow when measured in cents and widen when measured as beat rate. | moderate / moderate | K-21 |
| The higher of two voices is encoded better, in adults and in 7-month-old infants. Entries of inner voices are harder to notice than those of outer voices. | moderate / moderate | K-22 |
| In Bach, voices cross less than expected (less in denser textures), enter singly and exit together, and use intervals that promote fusion less than their consonance predicts. One composer, one tuning. | moderate / weak | K-23 |
| Timbre differences lower the pitch separation needed to split two lines. Attention can be switched between instruments in two-voice polyphony. | moderate / moderate | K-24 |
| Non-musicians heard quarter-tone dyads as neighbouring twelve-tone intervals (20 listeners). A new scale (Bohlen-Pierce, which has no octave) was learned from 25 to 30 minutes of listening; it may not carry over to octave-based divisions (G-24). | moderate / weak | K-25 |
| Neurons in cat auditory cortex respond more to a rare sound than to the same sound when common, with adaptation within seconds. The step to "a drone is cheap to track" is the lab's own (G-16, G-17). | strong / strong | K-26 |

### Melody, continuo, drone and the traditions

| What the sources report | Strength | Entry |
| --- | --- | --- |
| In vocal melodies from four continents a large interval tends to be followed by a change of direction, and tessitura alone can produce this. Skips cluster at the extremes of the range, more at the bottom. The expectation of a reversal after a skip is stronger in trained musicians, so it is at least partly learned. Whether any of this holds for maqam, Tuvan or Moroccan melody is open (G-20). | moderate / weak | K-27, K-28 |
| Tuvan throat singing is described as a low sustained fundamental with a high stream of harmonics. The melody lies between about the 6th and 12th harmonic with the 7th and 11th avoided, in a syntax that favours pentatonic melodies. The two parts are heard as one whole. Popular and encyclopedic accounts and one single-singer acoustic study. | weak / weak | K-29 |
| Moroccan Andalusi music is vocal-led and heterophonic; its main-voice melody was stable between 1932 and 2018 recordings. A nawba is a sequence of five mizan on a tab' (a mode-like unit). The Gnawa sintir has a drone string. Nothing on tab' tuning (G-02, G-08). | weak / weak | K-30 |
| In one qanun player's measured performance the neutral and microtonal degrees deviate substantially from 12-TET (abstract only, no cents values). Practitioners say the neutral third differs by region, era, maqam and musician, and is learned through melody, not as a fixed ratio. | weak / weak | K-31 |
| Sung Carnatic intervals fit 5-limit just intonation better than equal temperament (the source's correlations: 0.55 against 0.45); sung Hindustani intervals fit equal temperament better (0.72 against 0.64). There is no strong evidence for 22 shrutis. Two traditions, opposite verdicts: no single natural tuning is read off sung practice. | moderate / weak | K-32 |
| The rule of the octave is described as a keyboard harmonisation of a bass scale and a teaching device for realising a bass. A corpus study found its chords made up 67% (major) and 63% (minor) of Couperin's chords over bass degrees and about 49% and 46% in Corelli, and a list of the ten most common chords did better overall: only partly supported. | moderate / unrated | K-33 |
| Jazz theory states the avoid note in interval terms: a scale degree a half step above a chord tone, or a 9, 11 or 13 that does not build compatible chords for the mode. The two weak sources differ on cases (the Dorian 13) and give no acoustic reason. | weak / weak | K-34 |
| A 2025 proposal (abstract only) says Arab musicians and audiences have not accepted neutral intervals as chords because of low perceived concordance, and offers a tuning for concordant neutral thirds that keeps the maqam's pitch properties. No values, no listening test. | weak / weak | K-35 |

The 2025 proposal is the nearest thing found to counterpoint literature for these scales. No corpus of counterpoint inside the Moroccan, Gnawa, Amazigh or Tuvan traditions was found (G-28).

### Consonance across tunings, and the large projects

The first round's consonance record was thin exactly where the composer works: nothing had been read on how listeners judge sound in tunings other than twelve-tone. The second round read the studies below. They are the best that was found, and every one stops short of the composer's divisions. The records are in research/raw/ (strands T, P and W); the ledger entries are K-36 to K-44.

| Study (record, entry) | What it reports | Where it stops |
| --- | --- | --- |
| Marjieh et al. 2024 (T-01, K-36) | With harmonic tones the pleasantness of dyads swept over 0 to 15 semitones peaks near integer semitones; stretching the partial spacing moves the octave peak (12.04 semitones harmonic, 12.78 stretched). With a bonang-like timbre the reported peaks are at 2.60 and 4.80 semitones, with none detected at the major third or fifth. Online listeners from the US and South Korea; 235,440 judgments in all, per the abstract. | Pleasantness of isolated dyads and triads with synthetic tones; two national samples; the text read ended partway through the methods. It shows that timbre moves the peaks; it does not test chords in divisions above twelve. |
| Sethares 1993 (T-02, K-37) | The local minima of dissonance curves computed from a timbre's spectrum define scales that suit that timbre, and the reverse. The lab's roughness term is the Plomp and Levelt curve in Sethares's parameterisation. | A model; the page read gives no equations and no listener data (abstract only, weak). |
| Milne, Laney and Sharp 2016 (T-03, K-38) | 44 listeners, 2,638 forced-choice tests on 16-note melodies in eleven equal divisions of 3 to 17 notes per octave: the spectrum matched to the tuning was chosen in 61% of tests (95% CI 59 to 63%). A model of spectral pitch similarity plus harmonicity fits with r-squared .64 (cross-validated .61), a smoothing width of 10.53 cents (95% CI 8.40 to 12.66) and a roll-off of 0.58. | Single melodies with a manipulated timbre: no chords, no counterpoint; divisions 3 to 17 only; culture not reported, and the authors say acculturation cannot be ruled out; the model has no roughness and no masking. |
| Smit et al. 2019 (T-04, K-39) | Ratings of mostly unfamiliar Bohlen-Pierce triads by two groups of 60 listeners showed no effect of tuning (just intonation, 414 chords, against equal-tempered, 66 chords). Roughness, harmonicity, spectral entropy, dissimilarity from 12-TET triads and average pitch together explained 41.6% (consonance) and 47.4% (valence) of the variance. | A null result for these chords and listeners (mostly psychology undergraduates). The text read does not give how many cents the two tunings differ by, so it measures no tolerance in cents (G-24, G-26). Most of the variance is unexplained. |
| Harrison and Pearce 2020 (T-05, K-40) | On chord ratings from Bowling et al., a composite of interference, periodicity/harmonicity and cultural familiarity reached r = .88, against .77, .72 and .72 for the best single model of each kind. | Listeners and chords of all four datasets re-analysed are Western; the familiarity model is built from Western chord corpora (G-03); the weights are fitted to one dataset; read from a partial preprint. |
| Savage et al. 2015 and Mehr et al. 2019 (P-01, P-02, K-41) | Large comparative projects report statistical regularities, not absolute universals: 304 recordings from nine regions gave 18 statistical universals and a network of 10 associated features; an ethnographic corpus with a discography found three dimensions of variation (formality, arousal, religiosity) and more variation within societies than across them. | Coded categories and judged tonality; neither page read reports interval sizes in cents; nothing on counterpoint; P-01 read as an abstract only. |
| Cantometrics and SymbTr (P-03, P-04, K-42) | Cantometrics codes 5,776 songs on 37 categorical lines, among them the musical organisation of the vocal part and the polyphonic type. SymbTr holds 2,200 symbolic scores of Turkish makam music in a 53-comma notation. | A code is a coder's category for a recording; a score gives the pitch a theory assigns to a written note. Neither is a measured interval, and both are what a project collected, not samples of the world's music (G-29). |
| Erkomaishvili dataset and Bozkurt et al. 2009 (W-03, W-04, K-43) | Georgian three-voice singing is available as annotated tape recordings (a 1.1 GB dataset with CSV annotations and MusicXML transcriptions). A study of nine maqams compares pitches derived from recordings with the scale tones of theoretical models. | The dataset was not opened (G-29); the abstract of W-04 gives no result. Neither closes G-02. |
| Scherbaum et al. 2022 and Mauch et al. 2014 (W-01, W-02, K-44) | In 119 performances of Georgian three-voice songs by 19 ensembles, Gaussian-mixture models of the pitch distributions show pure fourths and fifths, a "neutral" third near 350 cents and a harmonic second systematically larger than the melodic one. In 72 recordings of one familiar tune by 24 solo singers the median absolute drift was 11 cents and the median note error 19 cents. | Both read through a fetch tool's extraction, so the numbers are the extractor's. W-01 is one tradition (14 of its 19 ensembles are Svan); W-02 is solo singers of a Western tune and says nothing about ensembles or drones. They bear on how far real intonation scatters (G-24), not on what a composer's synthesis should play. |

What this adds up to for the composer: the literature supports offering a choice of consonance model and exposing its weights and its tolerance (F5 in the fix list), and the lab already carries that structure. It supports no default for 19 or more divisions. The experiments stop at 17 notes per octave for melodies, use one non-octave scale, or use Western chords and listeners (G-30).

## Counts on real music, with the composer's output beside them

The first round compared the lab's models with recalled lists. This round counts real music with rules that are written down and tested (lab/10-corpus.js, 68 checks) and runs the same rules on what the composer plays. The composer rows are the shipped composer's scored default choice at nine divisions (12, 17, 19, 22, 24, 31, 41, 53, 72), twelve seeds each (chord start 0 to 3 crossed with eta 0 to 2), with no setting changed to move a number. Every statement is "in this collection": SymbTr is notation of a theory, not performed pitch; the chorales are one composer's harmonisations; Cantometrics holds coders' categories for recordings. A difference between the composer and a collection is printed as a question, never as a score. The raw collections are not kept in the project (size, licences); the small derived tables are, and a test rebuilds research/CORPUS.md from them. All nine sections of tables are in that file.

### The collections

| Collection | Version | Pieces or songs | What it holds |
| --- | --- | --- | --- |
| SymbTr | 2.4.3 | 2,200 | Turkish makam scores, single lines, in a 53-comma notation |
| Bach chorales, Palestrina, Monteverdi, Trecento (music21) | 10.5.2 | 371, 1,318, 49, 103 | Western polyphony in written twelve-tone pitches |
| Essen folk songs (music21) | 10.5.2 | 8,514 | Single melodic lines |
| Cantometrics (Global Jukebox) | commit 50f58b06, 2024-03-25 | 5,776 coded songs | Categorical codings of recordings on 37 lines |

### Melodic moves, by the role of the voice

A leap is a move of 250 cents or more, a step is a move under 250 cents, and a micro move is under 45 cents (the composer's own limits). Each figure is a share of the moves of that voice. Ranges run over the four Western collections, or over the nine divisions of the composer's output.

| Quantity | Four Western collections | One-line collections | Composer, shipped | Composer, with an existing setting |
| --- | --- | --- | --- | --- |
| Highest voice, leaps | 0.151 to 0.183 | SymbTr 0.157; Essen 0.321 | 0.320 to 0.411 | Smooth preset: 0.282 to 0.374 |
| Highest voice, steps | 0.542 to 0.728 | SymbTr 0.680; Essen 0.473 | 0.347 to 0.524 | Smooth preset: 0.465 to 0.640 |
| Inner voice, leaps | 0.189 to 0.275 | none | 0.283 to 0.389 | Smooth preset: 0.250 to 0.361 |
| Lowest voice, leaps | 0.257 to 0.340 | none | 0.655 to 0.976 | Walking bass: 0.355 to 0.438 |
| Lowest voice, steps | 0.391 to 0.649 | none | 0.024 to 0.119 | Walking bass: 0.414 to 0.532 |
| Lowest voice, moves in 12 pieces | none | none | 84 | Walking bass: 372 |

In the shipped output 0.226 of the highest voice's moves land on a chord change, and its leaps are not gathered there: its leap share is 0.286 to 0.357 for moves that land on a chord change and 0.316 to 0.444 for moves inside a chord.

### Neighbouring degrees and pitch classes used

A core pitch class is one that carries at least 5% of a piece's notes. The last column is the share of gaps between neighbouring core pitch classes of a piece that are under 45 cents.

| Collection or division | Pitch classes used per piece (first / middle / third quartile) | Smallest gap between core pitch classes, cents | Gaps under 45 cents |
| --- | --- | --- | --- |
| SymbTr (15,115 gaps) | 8 / 10 / 12 | 90 / 90 / 113 | 0.004 |
| Bach chorales; Palestrina; Monteverdi; Trecento | 10 / 11 / 11; 9 / 10 / 11; 11 / 11 / 11; 9 / 10 / 11 | 100 / 100 / 100 in each | 0 in each |
| Composer, 12 to 24 divisions | 7 / 7 / 7 (7 / 7 / 8 at 17) | 100, 70, 126, 55, 100 at 12, 17, 19, 22, 24 | 0 |
| Composer, 31 divisions | 8 / 8 / 9 | 78 / 116 / 116 | 0.024 |
| Composer, 41 divisions | 14 / 15 / 15 | 29 / 29 / 29 | 0.217 |
| Composer, 53 divisions | 14 / 14 / 15 | 22 / 23 / 23 | 0.208 |
| Composer, 72 divisions | 13 / 14 / 15 | 17 / 17 / 17 | 0.210 |

### How the songs are coded (Cantometrics)

| Question | Codes and shares |
| --- | --- |
| Line 4, musical organisation of the vocal part (5,776 songs coded; a song can carry more than one code) | Monophony 33.1%, Unison 29.4%, Polyphony 32.4% (1,872 songs), Heterophony 8.1%, Unrelated 0.6% |
| Line 22, polyphonic type, among the 1,872 polyphonic songs | Counterpoint 30.0% (561 songs), ParallelChords 26.5% (495), Harmony 18.5% (346), DronePolyphony 15.3% (286), IsolateChords 13.5% (253), NoPolyphony 1.1% (20) |

The project's own wording of the codes: Counterpoint is two or more parts that are rhythmically and melodically independent; ParallelChords is two or more parts moving parallel at pitch intervals other than the octave or unison; Harmony is "contrary motion occurs"; DronePolyphony is one or more tones held or repeated while the melody follows its own course.

### What these tables cannot say

- A collection is not a tradition. SymbTr is notation chosen and written by curators; the Western sets are written twelve-tone pitches; Cantometrics is a coder's judgement of each recording.
- Notation is not sound. SymbTr gives the pitch that a theory assigns to a written note (53 commas), not what was sung or played.
- The composer rows are twelve seeds per division. The spread between seeds is not shown, and a difference in the third decimal is not a finding.
- Phrase and form are not measured. The counts cover single moves, pitch classes and voice pairs.

## What the lab computes

The published composer decides which pitch a note has in three separate ways with no stated priority: the scale from a run of the division's own fifths, a chord's third from the best-fitting step near the third of that run, and the consonance class from a table of ratios. For the minor pentatonic scale the three name the same third in 31 of 61 divisions (12 to 72). That is arithmetic about the code, not about music (sketch S14).

The lab keeps these decisions apart. A frame (`08-frames.js`) states them once, as separate parts: grid, vocabulary, placement, reading, overrides, texture and provenance. An audit lists where the parts of one frame disagree. Each finding says what kind of statement it is and which settings move it.

| Layer | File | What it answers | Kind |
| --- | --- | --- | --- |
| Units and registry | `00-core` | Cents, Hz, small vector helpers, and the registry where every adjustable setting is listed with its status. | arithmetic, bookkeeping |
| Ear | `00-ear`, `00-eartime` | How wide the ear's filters are, the smallest audible pitch step, which partials stay audible next to a louder tone, which harmonics are resolved. `00-eartime` simulates the ear's front end in time to check the closed forms. | model |
| Scene | `00-scene` | How tones group into lines or objects a listener can follow, and a relative load figure. All weights are assumed. | model |
| Pitch | `01-pitch` | Where a scale comes from: cents, ratios, chains of fifths, nearest steps of a division. | arithmetic |
| Spectrum | `02-spectrum` | Tones as harmonic series; pitch-class spectra. | arithmetic, model |
| Consonance | `03-consonance` | Three ways of scoring how well two tones' partials line up, and roughness, side by side, with the composer's own measure for comparison. | model |
| Stability | `04-stability` | How well each tone fits a reference sound. | model |
| Sonority | `05-sonority` | Which groups of scale degrees count as sonorities; tension against a chord; the avoid-note switch (off by default). | model |
| Melody | `06-melody` | How one voice moves: step, leap and inflection classes in cents or in scale degrees; a small generator with no reversal rule. | model, arithmetic |
| Texture | `07-texture` | Drone and basso continuo. The rule-of-the-octave table is kept as replaceable data, marked recalled. | model |
| Frames | `08-frames` | One place that declares grid, vocabulary, placement, reading and texture; presets; the audit; a sweep over divisions. | each finding carries its kind |
| Listener | `09-listener` | Reads one person's listening-lab export into overrides by layer. | bookkeeping |

Nothing in the lab draws or plays; every module runs under Node. The published composer's modules are read, never changed, so that a frame in the legacy reading can be checked against the composer number for number.

## Open gaps

Twenty-four things are not known: the twenty-two in this table, and two added in the second round (G-29 and G-30) in the table below it. For each, the table says what is missing, what would settle it, and which settings carry it, so that you can change them in the meantime. The lab fills none of them with a model. The identifiers (G-02 and so on, and the record codes such as M-07) are those of `research/LEDGER.md`.

| Gap | What is not known | What would settle it | Settings to tune meanwhile |
| --- | --- | --- | --- |
| G-02 | Which ratios or cents the neutral degrees of Rast, Bayati and Sikah, and their Moroccan counterparts, have in performance. The lab's presets (11:9, 12:11 and so on) are its own constructions, and M-07 says no single value exists. | Measured pitch tracks of recordings (the full text of M-02, the sources M-07 draws on, a corpus of Moroccan Andalusi recordings), reported as distributions and not as one number per degree. | `pitch.snapTolC`, `scene.catTolC` |
| G-03 | Corpus familiarity outside twelve tones: what a listener of a given culture has heard, as a distribution over intervals. Models fitted to ratings use it as one of three terms (Q-02, recalled); none exists for a 53-division or maqam listener. | Interval statistics of a corpus in the target tradition, or the listener's own calibration in the listening lab (no sheet for it yet). | `cons.wFam`, `cons.famSigmaC` |
| G-05 | How a drone changes which intervals are tolerated or preferred in the voice above it. The lab's drone ladder (levels 0 and 1) scores stability against the drone; no measurement says that listeners do this. | A listening experiment: ratings of melodic intervals over a sustained fundamental, by drone spectrum (no sheet for it yet). | `tex.droneMinGain`, `stab.ref` |
| G-06 | Measured drone spectra with numbers (partial amplitudes of the tambura, the Tuvan fundamental, the sintir drone string). A drone is a spectrum, and its partials decide which melodic tones fuse with it. | Spectral analysis of recordings; the full text of D-05. | `spec.nPartials`, `spec.rolloff`, `stab.ref` |
| G-07 | How and when drones change; the structure of ostinato and ground basses; drone polyphony. Drone levels 2 to 4 are not built because nothing read describes them. | Analytic literature on drone change in specific repertoires; a transcribed corpus. | none |
| G-08 | Gnawa and Amazigh pitch material and texture. Sum (2011) and Schuyler (1979) were reached only as bibliographic records, and the sintir entry (M-06) names no ostinato. | Read Sum 2011, Schuyler 1979 and Lortat-Jacob's work on the High Atlas; a transcription corpus. | none |
| G-10 | Whether the auditory filter width in the bass follows the Bark (critical-band) curve or the ERB law. In the lab's model the two differ most below about 500 Hz, and the roughness there differs by a factor of two (S9, S12). | The primary sources: Glasberg and Moore 1990, Zwicker's critical-band data, Plomp and Levelt 1965 read in full. | `ear.widthLaw`, `ear.bwScale` |
| G-12 | The tonal-masker offset and its level dependence (a tone masks less than noise by several dB). It decides how many partials of a quiet voice are audible next to a loud one (S11, model). | Masking-pattern studies with tonal maskers; the constants of the MPEG psychoacoustic model read in full. | `ear.maskOffsetDb`, `ear.upperSlope` |
| G-14 | Precision of vocal motor control of pitch: how accurately singers hit and hold a pitch, in cents. This is the "motor" half of the request; it would set a lower bound on useful step size for singers, as against listeners. | Singing-accuracy studies (cents of error, with and without feedback). | `pitch.stepTolC` |
| G-16 | The attentional cost of following a drone. The scene layer discounts a predictable object, but no study measured what a drone costs. | A tracking or divided-attention experiment with and without a drone. | `scene.predictDiscount`, `scene.predictAfterMs` |
| G-17 | The mapping from predictability to tracking cost. A repeating sound adapts in cat cortex (K-26), but the size and form of the saving in following a musical voice is unknown. | A tracking experiment as in G-16, with the predictability of the drone varied. | `scene.predictDiscount` |
| G-18 | The capacity for simultaneous streams when the timbres differ. All the voice-counting data are for homogeneous timbres; the lab has one synth recipe and a timbre weight set to zero for it. | Voice-counting and tracking experiments with mixed ensembles. | `scene.maxStreams`, `scene.wTimbre`, `scene.wHarmDiff` |
| G-19 | A definition of "auditory object" that can be measured. The lab's object is a threshold on a weighted sum of cues, and in sketch S13 (a model result) the counts depend on that threshold more than on anything else. | The proposed definition in the full text of A-14, and experiments that calibrate the threshold by ear. | `scene.segThreshold` |
| G-20 | Tessitura and mobility regularities in microtonal modal repertoires and in polyphonic inner voices. V-01 to V-05 are vocal samples, Western or cross-cultural; whether post-leap reversal and the descend-small, ascend-large asymmetry hold for maqam, Tuvan or Moroccan melody is not addressed. | Interval and range statistics of transcribed melodies in these repertoires, reported by their authors. | `melody.rangeC`, `melody.wRange`, `melody.wProx` |
| G-21 | The shape of the phase-locking roll-off in humans, and the order of the filter that models it. It decides how much temporal information the high partials contribute; N-01 gives only a range, 1.5 to 10 kHz. | Primary physiological and psychophysical studies of human pitch limits. | `ear.plOrder`, `ear.plCutHz` |
| G-22 | The weights of the segregation cues against each other for polyphonic music, and the pitch separation at which two notes are half segregated. No source weighs the cues. | The listening lab: you adjust to where you hear separate lines (sheet 3). That gives one listener's value, not an answer. | `scene.wPitch`, `scene.wOnset`, `scene.wFusion`, `scene.wTimbre`, `scene.wMotion`, `scene.sep50Erb`, `scene.sepShape` |
| G-23 | The salience of the bass voice relative to the inner and top voices. High-voice superiority is established (K-22); nothing read ranks the bass. | Two- and three-voice deviant-detection studies with the bass as the target. | `scene.roleBass` |
| G-24 | How many categories a scale can hold, and how wide each category is, outside twelve tones. A-10 and A-11 bear on it weakly and for other scales. | Categorical-perception experiments with listeners of the target tradition, and category widths from a corpus. | `scene.catTolC`, `scene.absIdBits` |
| G-25 | The unit of "step", "skip" and "leap" in scales with unequal gaps and in different divisions: scale degrees or cents. Arithmetic: at the published composer's 250-cent threshold the 300-cent gap of a minor pentatonic scale is a leap, and in 72 divisions one step (16.7 cents) is below its 45-cent inflection limit. Which unit a tradition's own regularities follow is not known. | A decision per tradition frame; transcribed melodies would show which unit the repertoire's own regularities follow. | `melody.stepUnit`, `melody.stepMaxDeg`, `melody.skipMaxDeg`, `melody.stepMaxC`, `melody.skipMaxC`, `melody.microMaxC`, `melody.wReverse` |
| G-26 | How far a neutral degree may be tempered to give a concordant vertical interval before it stops being that degree. M-08 proposes "perceptual tempering" without values; the builder's snap parameters are exactly this trade. | The full text of M-08; categorical-perception experiments on neutral thirds; the listening lab (one listener, sheet 2). | `pitch.snapTolC`, `pitch.snapLambda`, `scene.catTolC` |
| G-27 | The part of the jazz avoid-note rule that the ear model lacks: why a tension a half step above a chord tone is avoided and one a half step below is not. In the lab's model (S15) the two give nearly the same roughness, by construction (a compound minor ninth against a major seventh, ratio 0.98); the rule treats them differently and no source read says why. | Perceptual work on chord-tone identity and tension; corpus counts of held tensions; the full chord-scale text. | `sonor.avoidAbove`, `sonor.avoidRel`, `sonor.tensionAboveC` |
| G-28 | Contrapuntal practice inside the Moroccan, Gnawa, Amazigh and Tuvan traditions. No corpus of it was found; the records read describe heterophony, drone with overtone melody, and a drone string. Rules for a three-voice automaton on these scales are an inference from the ear and scene layers and from classical and jazz practice, not a description of the traditions. | Ethnomusicological analyses of multi-part practice (Ahwash, Gnawa lila, Tuvan ensembles); composers' own accounts of polyphonic maqam writing (M-08, M-09). | none |

Added in the second round:

| Gap | What is not known | What would settle it | Settings to tune meanwhile |
| --- | --- | --- | --- |
| G-29 | Vertical intervals (voice against voice, in cents) of polyphonic singing or playing in tunings other than twelve-tone, measured on recordings or on scores whose notation gives performed pitch. The collections counted in the second round hold either single melodic lines in 53-comma theory notation (SymbTr) or written pitches in twelve-tone notation; only W-01 reports harmonic intervals from performances, for one tradition. | Open the Erkomaishvili dataset (W-03) and the corpus behind W-01 and count the simultaneous intervals of the three voices; find or build annotated recordings of other polyphonic traditions; report distributions, not one number per interval. | pitch.snapTolC, scene.catTolC, cons.model |
| G-30 | How listeners rate chords and counterpoint in equal divisions of 19 or more notes per octave, and in tunings of their own tradition. The experiments read stop at 17 notes per octave for melodies (T-03), use Bohlen-Pierce triads (T-04), or use Western chords and listeners (T-05); the composer offers 19, 22, 24, 31, 41, 53 and 72. | A listening experiment (the listening lab is the start): chords and short counterpoint in 19, 31 and 53 divisions against their just-intonation or twelve-tone counterparts, with listeners from more than one tradition, recording ratings and the mistuning in cents that listeners accept. | cons.model, cons.wFam, pitch.snapTolC |

G-28 and G-02 sit under the others. Until the first is closed, any rule for the three voices is the lab's inference; until the second is closed, the neutral degrees are the lab's construction. The listening lab's sheets bear on G-22 (sheet 3) and, for one listener, on G-24 and G-26 (sheet 2); they settle none of the three. No sheet exists yet for G-03 or G-05.

## Settings you can tune

Every adjustable number in the lab is a registered setting with a label, a unit, a default, a range, a status and the records it rests on (`lab/00-core.js`; `TF.registryJSON()` lists them all). There are 125. The status says what stands behind the default.

| Status | What stands behind the default | Settings |
| --- | --- | --- |
| measured | A number from a measurement that a fetched record contains. | 4 |
| literature-range | Sources give a range; the default is one point inside it. | 16 |
| model-derived | Follows from other settings through the model's own definitions. | 2 |
| engine-legacy | What the published composer does today, kept so that the lab can reproduce it. | 6 |
| assumption | The lab's own choice. Nothing measured it; it is to be set by ear or from a corpus. | 97 |

Ninety-seven of the 125 are assumptions, and those are the ones to change first. By layer the count is: `scene` 26, `ear` 24, `cons` (consonance) 14, `melody` 13, `eartime` 10, `sonor` (sonority) 9, `stab` (stability) 7, `prog` (progression scoring, in `05-sonority.js`) 6, `tex` (texture) 5, `frame` 5, `pitch` 3, `spec` (spectrum) 3.

### How to change one

A module that uses settings takes an object `F` with one entry per layer, the same shape as the overrides of a frame: `{ear: {bwScale: 0.6}, scene: {catTolC: 30}}`. An example: `TF.ear.bandwidth(440, {ear: {bwScale: 0.6}})` gives the lab's filter width at 440 Hz with that factor. `TF.opts(layer, over)` checks the object first. An unknown name, a value that is not a number, a value outside the registry's range, or an option that does not exist stops with an error in words, so a mistyped setting cannot slip through. Nothing is stored; the registry's defaults are the same after every call, and the published composer is not touched.

To add a setting, `TF.def(layer, name, {label, unit, def, min, max, step, status, refs, note})`. A `measured` or `literature-range` setting must cite a record; an `assumption` must cite something or explain itself in its note. The tests fail on a reference that does not resolve, on an identifier cited anywhere that does not exist, and on a gap that nothing cites.

### Your five settings from the listening sitting

The export you sent (one listener, one device, one sitting) was read with `TF.listener.fromExport`. All five settings were accepted, none was left out, and one sits exactly on an end of the registry's range. These are your own copies of settings the lab had to assume. They are not measurements of anyone else, and they say nothing about any musical tradition.

| Setting | Unit | Registry default (status) | Your sitting | Mark |
| --- | --- | --- | --- | --- |
| `ear.untrainedFactor` | multiple of the practised value | 6 (measured, E-06) | 1.02 | none |
| `scene.catTolC` | cents | 50 (assumption) | 30 | rough: your answers crossed one half more than once |
| `scene.sep50Erb` | ERB | 2.5 (assumption) | 0.5 | clamped: the sheet gave 0.15, which is below the registry's minimum of 0.5 |
| `ear.beatMaxHz` | Hz | 20 (literature-range, E-13) | 14 | none |
| `ear.bwScale` | multiple of the lab's filter width | 1 (literature-range, E-09, E-10) | 0.6 | rough: your answers crossed one half more than once |

The file was exported before the export carried marks, so the two "rough" marks come from the lab's own logic read over the counts in the file. The pitch factor in the file is 1.02, and the same logic over the file's two-decimal counts gives 1.01; that is rounding in the older export (the export now keeps four decimals), and the file is kept as it was.

One setting was added by the loader and not by you. `ear.listener` has two options, "practised" (the default) and "untrained", and the pitch factor is used only when it is "untrained", so loading a file that gives the factor sets it, and says so in the notes it returns. With a factor of 1.02 the two give nearly the same smallest audible pitch step.

## The listening lab

[The listening lab page](https://claude.ai/artifact/HrcE6gNpWM5hBm5xhGuoor) hands the settings marked assumption to a listener's own ears. It is private to you until you share it. Its code is in `lab/listening/` and the built page is `lab/listening/out/listening-lab.html` (150 KB). Four short sheets give five of the lab's settings a number from one person on one device, and a fifth sheet plays one scale placed three ways. Nothing the page produces is applied anywhere; you decide what to do with it.

| Sheet | What you do | What it sets | Default (range, status) |
| --- | --- | --- | --- |
| 1 Smallest pitch change | Hear two notes in turn and say which way the second moved. After two right answers in a row the change gets 1.5 times smaller; after a wrong one it gets 1.5 times larger. Three registers: C3, C4, C5. | `ear.untrainedFactor`: your threshold at 261.6 Hz divided by the lab's practised value there | 6 (1 to 10, measured, E-06) |
| 2 Same note or different | Hear a short scale, then one of its notes, then that note moved a little sharp or flat, and say whether it is the same note. Offsets from 10 to 100 cents, two answers each. | `scene.catTolC`: the offset at which half the answers are "same note" | 50 cents (10 to 200, assumption) |
| 3 One line or two | Hear a low, high, low gallop and say whether it is one line or two. Gaps from 0 to 1200 cents, two answers each. | `scene.sep50Erb`: the gap at which half the answers are "two lines", in filter widths | 2.5 ERB (0.5 to 6, assumption) |
| 4 Wobble, buzz or two tones | Hear two plain tones together for two seconds, 3 to 90 Hz apart, the lower near 440 Hz, and say slow wobble, fast buzz or two smooth tones. Two answers each. | `ear.beatMaxHz`: where "slow wobble" falls to half. `ear.bwScale`: where "two smooth tones" rises to half, divided by the lab's filter width at that pitch | 20 Hz (5 to 40, literature-range, E-13). 1 (0.5 to 3, literature-range, E-09, E-10) |
| 5 The mixup | Hear one scale on a chosen division placed three ways, then a blind A/B comparison. Nothing is scored. | none | none |

### What your first sitting gave

These are the counts from the export you sent. They are what one person answered: not source reports, not model results, and not findings about anyone else or any tradition.

| Sheet | Your answers | The lab's number from them | Mark |
| --- | --- | --- | --- |
| 1 | One run per register: 3.51 cents at 130.8 Hz (29 trials), 3.51 at 261.6 Hz (34), 4.92 at 523.3 Hz (34). The lab's practised value at 261.6 Hz is 3.46 cents. | Factor 1.02 | none |
| 2 | "Same note" said 2, 2, 1, 1, 0, 1, 2, 1 times out of 2 at 10, 20, 30, 40, 50, 65, 80 and 100 cents. | 30 cents (between 20 and 30) | rough |
| 3 | "Two lines" said 0 of 2 at 0 cents and 2 of 2 at each of the other seven gaps, 100 to 1200 cents. | 0.15 filter widths (between 0 and 0.29); the setting takes 0.5 | clamped |
| 4 | "Slow wobble" said 2, 2, 2, 1, 1, 0, 0, 0, 0, 0 times out of 2 at 3, 6, 10, 14, 18, 24, 32, 45, 65 and 90 Hz. "Two smooth tones" said 0 of 2 everywhere except 1 at 45 Hz and 2 at 90 Hz. | Wobble: 14 Hz (between 10 and 14). Two tones: 45 Hz, which is 0.6 of the lab's filter width there (74.6 Hz) | the two-tone number is rough |
| 5 | Two blind comparisons, both "no difference I can hear": 53 steps, minor pentatonic scale, tonic chord at 131 Hz, six overtones, the chain of the division's fifths against simple ratios. | none | none |

### What this can and cannot tell

- **Thin counts.** Sheets 2 to 4 have two answers per level. The half-way point is a straight line between two levels, so one changed answer moves it by a whole level. On sheets 2 and 4 the answers do not fall in a steady order ("same note" goes 0 of 2 at 50 cents, then 1 of 2 at 65 and 2 of 2 at 80). The lab marks such a number rough and does not choose a reading. The counts alone do not say whether that is a slip, a feature of the ear, or the device.
- **Sheet 1 has a coarse step.** The staircase moves by a factor of 1.5, so one run cannot tell 3.46 from 3.51 cents. The factor 1.02 reads as "about the practised value" and nothing finer.
- **Sheet 3 cannot place this listener.** The first gap above zero is 100 cents, and the answers were already "two lines" there, so the half-way point lies somewhere in the first gap. The straight line gives 0.15 filter widths, below the registry's minimum of 0.5, so the setting was clamped. Finer levels would not change the clamped value unless the minimum is lowered. That is a decision for the integration plan; the registry is unchanged.
- **The audition said nothing.** The two placements put the third of the chord 22.64 cents apart (one step of the 53 division, about 155.1 and 157.1 Hz at a tonic of C3, 130.8 Hz), and the notes sent to the speakers differ by that amount, so "no difference" is not a playback fault in the lab's code. Whether register, overtone count, device or listener is the reason has not been tested.
- **One listener, one device.** The device was a pair of Bluetooth speakers and the sitting lasted about 19 minutes. No other listener has used the page.

### Saving and loading

The page saves each answer as it is given, one document at a time, to the page's store for your account, and falls back to the browser's own storage if the store is unavailable; the page says which one it is using. I confirmed the store route by reading back the documents your sitting wrote (pitch, category, stream, beat and audition). The route that gives you the settings as a downloaded file was not confirmed in the real viewer.

`TF.listener.fromExport(text)` (`lab/09-listener.js`) turns an export into overrides by layer, the shape of a frame's `F`. It checks every identifier against the registry and every value against its range, and it lists what it did not take and why. It also returns the settings that sit exactly on an end of the range and the marks the file carries. One file is one person, one device and one sitting; nothing merges or averages files. Your file is kept as it was exported in `research/listeners/2026-11-01-bluetooth-speakers.json`, and the loader takes all five of its settings.

## What was checked, and what could not be

### Checked

- **Sources re-read.** 18 of the 87 records were fetched a second time against the numbers the code uses (`research/VERIFY.md`, 28 October). 16 held as recorded, six of them with a detail added. Two were corrected. E-08: the 1% to 3% mistuned-partial threshold belongs to tones of 410 ms, and the code had it at 1610 ms, so the default `ear.mistuneRefMs` is now 410. N-03: about three semitones is the spread of the individual means of ten musicians, not a difference between listeners. `scene.roleTop` and `scene.roleInner` moved from literature-range to assumption, because no number in them came from a source.
- **Code.** All eleven suites pass, 495 checks, run again today. Five of them (consonance, pitch, sonority, melody and texture, frames) also load the published composer's own modules, read-only, and compare.
- **The tests themselves.** Twelve deliberate breakages of the listening logic and the loader (rounding the export's thresholds to two decimals, never setting the rough mark, dropping the range check, and so on) were run against their suites. Ten fail a check and two stop the run with an error; none went unnoticed. One was missed in the first round (turning points rounded to two decimals), and a check was added for it.
- **The page.** 86 checks run the built page in Chromium with artificial listeners. A fresh build from the sources is identical to the file on disk, and the published page contains that file verbatim inside the wrapper the artifact tool adds. Saving to the page's store was read back in the real viewer.
- **Your file.** Recomputed from the counts in it, four of the five settings come out identical. The pitch factor comes out as 1.01 where the file has 1.02, because the older export rounded thresholds to two decimals; the export now keeps four, and your file is kept as it was.
- **The published composer.** A fresh build from `src/` is byte-identical to the `contrapunctus.html` delivered on 18 October, before this research began. The lab only reads the composer's modules.

| Suite | Checks | What it covers |
| --- | --- | --- |
| consonance | 36 | The three consonance scores, roughness, and the composer's own measure beside them |
| ear (closed forms) | 77 | Filter width, smallest audible pitch step, masking, which partials are audible |
| ear (time domain) | 21 | The time-domain simulation against the closed forms |
| frames | 65 | Frames, presets, the audit, the sweep over divisions |
| ledger | 28 | Every reference resolves, every gap is cited, and no statistics words appear in the named files or in finding text |
| listener files | 22 | The loader and the kept export |
| listening lab | 90 | The page's arithmetic: stepping rule, half-way finder, settings, export |
| melody and texture | 40 | Step, skip and inflection classes, the small generator, drone and continuo |
| pitch | 20 | Cents, ratios, chains of fifths, nearest steps of a division |
| scene | 57 | Grouping of tones into lines, the relative load figure |
| sonority | 39 | Sonorities, tension against a chord, the avoid-note switch |

### Could not be checked

- **A different reader.** Every re-read used the same fetch tool, a second reading of the same page by the same kind of reader. It can catch a number or a condition written down wrongly. It cannot catch an extraction that is wrong the same way twice, or an error in a paper.
- **The primary papers.** Of the 87 records, 33 rest on an abstract, 4 on a search snippet, and 50 on a fetched full text, some of it partial (each record says what was missing). 69 records have not been re-read. The 42 recalled items (Q) were not fetched and are not evidence; where a setting depends on one, its note says so.
- **Listeners.** One listener, one device, one sitting. There is no panel, no calibrated playback, and no listener from any of the traditions.
- **Fonts.** The page asks Google Fonts for IBM Plex. The tests ran without them, so the page with its own fonts has not been exercised.
- **The download route.** The route that gives you the settings as a downloaded file was not confirmed in the real viewer.
- **Whether the defaults are right.** 97 of the 125 settings stay assumptions until a listening test or a corpus changes them. The checks above show that the code does what the settings say, not that the settings are right.

## What this cannot conclude

These are ten things a reader might expect the lab to conclude. It does not, and each row says why.

| Not concluded | Why |
| --- | --- |
| Which tuning a Moroccan or Tuvan musician uses for a given degree. | No measured performance data was read for the neutral degrees (G-02), and nothing in the model can stand in for it. |
| Counterpoint rules inside the Moroccan, Gnawa, Amazigh or Tuvan traditions. | No corpus of such practice was found (G-28). The sources describe heterophony, drone and melody, not rule-governed counterpoint. |
| That the jazz avoid-note rule is explained by roughness. | The model's roughness cannot tell a tension a half step above a chord tone from one a half step below, by construction; the rule does (G-27). |
| That the rule of the octave follows from stability and consonance. | The sources call it a teaching device (K-33). The lab stores it as a table marked recalled (Q-13), which can be replaced. |
| That the Tuvan avoidance of the 7th and 11th harmonics follows from consonance. | K-29 reports the avoidance, from weak sources. The model's numbers for each harmonic are shown in sketch S5 with no conclusion drawn. |
| That divisions finer than some number add no new scale categories. | How many categories a scale can hold outside twelve tones is open (G-24). That a single step is smaller than the smallest audible difference a source reports for pure tones is arithmetic against that source's number. It is not a statement about categories. |
| Which of several equally coherent definitions of a scale a tradition uses. | Four definitions of the minor pentatonic put the third in different places in most divisions (S16). No listener or corpus decides between them (G-24, G-26). |
| That an assumed setting is right because a result looks sensible. | Assumptions stay marked as assumptions until a listening test or a corpus changes their status. The listening lab is for that. |
| That the composer's output is wrong where it differs from a collection. | The tables set counts side by side and stop. The collections are theory notation (SymbTr), written pitches in twelve-tone notation (the Western sets) and coders' categories (Cantometrics); none is microtonal polyphony (G-29). A difference is a question. |
| That any option on the fix list sounds better. | No listener has judged the composer's output at 19 or more divisions (G-30). The closest data are melodies in up to 17 divisions (T-03) and Bohlen-Pierce triads (T-04). |

Earlier sketches did draw conclusions of this kind. They were rewritten after the review of 30 October, and `research/CLAIMS.md` lists what each one said and what it says now.

## Fix list

research/FIXES.md holds the full list. Each item is an option someone can switch on. Nothing is built, the published composer is unchanged, and every default is the current behaviour. The counts are copied from research/CORPUS.md, and a test checks that every number in the list is in it. A difference from a collection is a question, not a target, and no value was fitted to a table.

| Item | What was counted | Option (exists, or proposed) | Default | Meets the integration plan |
| --- | --- | --- | --- | --- |
| F1 The lowest voice | One note per bar: leaps are 0.655 to 0.976 of its moves against 0.257 to 0.340 in the lowest voices of the four Western collections, steps 0.024 to 0.119 against 0.391 to 0.649. With the existing walking-bass switch (a bass note on every beat) leaps are 0.355 to 0.438 and steps 0.414 to 0.532. | Exists: the walking-bass switch. Proposed: the number of bass notes per chord (one, two, four) as a setting instead of an on/off box. | One note per chord, walking bass off. | Near step 5 (texture: the continuo option) |
| F2 The upper voices | The highest voice leaps in 0.320 to 0.411 of its moves against 0.151 to 0.183 in the Western collections (0.157 in SymbTr, 0.321 in the Essen songs). In each Western collection the highest voice leaps least of its three roles; in the shipped output it leaps more than the inner voice at all nine divisions. The Smooth preset gives 0.282 to 0.374. | Exists: the Smooth preset and Fine control. Proposed: weights by role (highest, inner, lowest). | One set of weights for all voices. | Not in the plan |
| F3 Two neighbouring degrees in one piece | At 41, 53 and 72 divisions 0.217, 0.208 and 0.210 of the gaps between neighbouring core pitch classes are under 45 cents (SymbTr 0.004, Western collections 0), and 14 / 15 / 15 pitch classes are used per piece at 41 against 7 / 7 / 7 at 12 to 24 and 8 / 10 / 12 in SymbTr. In the code the scale is a chain of fifths, while chord thirds come from a search within 45 cents for the best-fusing step (pickThird); the two differ by one step (29.3, 22.6 and 16.7 cents). | Proposed: expose the three constants of pickThird (reach 45 cents, gain 0.15, floor 0.5; a reach of 0 gives the scale's own thirds), and a placement setting for the scale builder (chain, nearest 5-limit ratios, rounded twelve-tone degrees). The lab's snap settings pitch.snapTolC and pitch.snapLambda carry the same two dials. | Chain scales; pickThird as shipped. | Steps 1 and 2 |
| F4 Texture | Cantometrics, among polyphonic songs: Counterpoint 30.0%, ParallelChords 26.5%, Harmony 18.5%, DronePolyphony 15.3%, IsolateChords 13.5%. The composer's voices move in parallel by the same cents in 0.001 to 0.014 of voice-pair moves against 0.040 to 0.082 in the Western collections; it has no drone and no heterophony. | Proposed extensions, not corrections: a parallel weight, a drone, heterophony. | The current texture. | Step 5 (drone levels 0 and 1) and step 8 |
| F5 The consonance function | By the composer's own function 0.716 (N=17) to 0.851 of dyads are consonant, against 0.859 to 0.891 in the Western collections. The function takes an interval in cents alone and assumes a generic harmonic tone of 6 partials. | Proposed: the model and its weights as settings (the lab has cons.model with ratioGaussian, template, blend and acf; cons.wFam; frame.consYes). | The current function, with 0.5 as the limit. | Step 3 |

Six counts point at no option. The next move goes back after a leap in 0.429 to 0.750 of cases against 0.519 to 0.716 (the ranges overlap, and the composer has a term for it). Parallel motion to a perfect interval is 0 against 0.000 to 0.030 (the composer forbids it by design). Voices cross in 0 against 0.038 to 0.466 (a design choice that the counts do not argue with; K-23, K-16). Contrary motion is 0.212 to 0.235 against 0.190 to 0.261. Repeated four-interval shapes in the first 16 notes are 0 to 0.024 against 0.019 to 0.056 (phrase and form are not measured). The composer's 12, 11 and 16 distinct move sizes at 41, 53 and 72 divisions are of the same order as SymbTr's 11 (the Western collections have 5).

### What the list cannot do

- It does not rank the options; the data for that do not exist. The order of work that research/FIXES.md suggests (F3 first, then F2 and F1, then F5 and F4) is a judgement about effort and risk.
- It does not say that any option sounds better. No listener has judged the composer's output at 19 or more divisions (G-30).
- It is not a statement about any tradition. The collections are notated Turkish makam scores, coded songs and the Western files bundled with music21; none is microtonal polyphony (G-29).
- Where F3 is concerned, the column "gaps under 45 cents" falls to about 0 by construction once the option is on, so it cannot show that the option helped. The list names the columns that can fail instead: the highest voice's leap share inside a chord at 41, 53 and 72 divisions, the consonant share, and the lab's audit of the composer (S14), then a listening comparison.

Nothing needs deciding to keep the composer as it is. If you want one option built first, the list's suggestion is F3: the counts point at one function in the code, and steps 1 and 2 of the plan already cover it without naming a tradition.

## Integration plan

The plan keeps the published composer's behaviour as the default and adds the lab's layers as options, one at a time. No step turns an assumption into a default. The guard for the classic path already exists: the composer's own suites (484 node checks and 236 browser checks, both passing today on the unchanged composer) and the golden file in `test/choice.js`, which requires that the classic choice plays exactly the pieces the first two versions played, from 12 to 72 divisions. The fix list before this section says which behaviours of the composer the second round's counts point at: F3 meets steps 1 and 2, F5 step 3, F1 and F4 step 5 (F4 also step 8), and F2 is not in the plan.

| Step | What changes in the composer | Check before moving on |
| --- | --- | --- |
| 1 One frame | The composer's three separate decisions (the scale from a run of the division's fifths, the chord third from the best-fitting step, the consonance classes from a table) are declared in one place. The default frame, "classic", reproduces them exactly. | The 484 and 236 checks pass unchanged, the golden file still matches, and the lab's audit of the composer (S14) prints the same table as before. |
| 2 Placement as a choice | A control for how scale degrees and chord thirds are placed: chain of fifths, simple ratios, snapped within a stated tolerance, or the composer's current snap. The lab has written and compared four definitions (S16). Classic stays the default. | For every division from 12 to 72, "classic" returns the degrees the published build returns, and each other option returns what the lab's `01-pitch` returns, compared number for number in a test. |
| 3 Reading as a choice | What counts as a step, a category and a consonance: the step unit (G-25), the category width (G-24) and the consonance model (G-03), each with its status shown beside it. | Under classic the golden file is unchanged. Under any other reading, the lab's audit for that frame lists where the declared choices disagree, and the composer shows that list. |
| 4 Ear options | Off by default. The lab's smallest audible step and masking decide which motions and partials count. The composer already uses a 45-cent limit and a roughness gate (`09-psy.js`). | Off: the golden file is unchanged. On: the composer's numbers equal the lab's `00-ear` numbers for a fixed list of cases. |
| 5 Texture | A basso continuo option whose figure table (the rule of the octave) is replaceable data marked recalled (Q-13), and drone levels 0 and 1. Levels 2 to 4 are not built (G-07), and what a drone does to the voices above it is an assumption (G-05, G-06, G-16). | Off: the golden file is unchanged. On: the numbers equal the lab's `07-texture` for fixed cases, and every option shows its status. |
| 6 Scene readout | The scene layer as a readout only: how many objects a listener could follow at this step under the current settings. It does not change the composition, because every weight in it is assumed (G-19, G-22). | The readout equals the lab's `00-scene` numbers for fixed cases, and the composition is identical with the readout on and off. |
| 7 Listener file | Paste the text from the listening lab's "Your settings" tab. The composer shows each setting with its default and marks, and applies them as overrides to the layers above. Files are never merged. | The lab's 22 loader checks carry over, a state code keeps the overrides through a round trip, and with no file the golden file is unchanged. |
| 8 A tradition frame | A data file for one tradition: scale, ratios or cents given as alternatives, category widths, texture, each field carrying its status. Fields that no source supports are labelled assumption or gap and left tunable. The frame does not claim to be the practice of the tradition (G-28). | The frame's audit prints every statement with its kind, a new test refuses a field that has neither a status nor a record, and each value can be traced to a record or to the word "assumption". |

Steps 1 to 7 depend on no gap being closed and need no tradition. Step 8 depends on the first decision below.

### Decisions for you

| Decision | Options and what each costs |
| --- | --- |
| D1 Which frame comes first | A neutral frame, with no tradition named (steps 1 to 7 only). A Moroccan Andalusi frame, which rests on weak sources and on G-02 and G-28. A Tuvan frame, which rests on K-29 (weak) and on G-06 and G-07. A Gnawa or Amazigh frame, which rests on one encyclopedia entry and on recalled statements (G-08), the thinnest record of the four. |
| D2 Whether one listener's numbers become defaults | Keep them per listener: the registry keeps the lab's assumptions and a file overrides them. Or make your own numbers the defaults of your copy of the composer. One sitting on Bluetooth speakers is thin, and a default would hide that. |
| D3 Sheet 3's resolution | Leave it, and clamped values stay marked. Or lower the minimum of `scene.sep50Erb` (now 0.5) and add gaps finer than 100 cents to the sheet, so that a listener like the first sitting (0.15) can be placed. That changes a registry range and the page; the default stays 2.5 and the tests are updated. |
| D4 The unit of a step (G-25) | Cents, as in the published composer (250 and 45 cents). Scale degrees. Or selectable per frame, with classic staying in cents. |
| D5 How much of the lab goes into the single file | The lab's modules total about 215 KB against 445 KB for the composer, and `08-frames.js` alone is 61 KB. Bring in every layer, or only the layers that the options in use need. |
| D6 What to do next besides integration | More reading toward G-02 and G-28 (the full text of M-02, M-08 and M-09, Sum 2011, Schuyler 1979, Lortat-Jacob). More listening: a second sitting on headphones, other listeners, and sheets for drone ratings (G-05) and familiarity (G-03). Neither blocks steps 1 to 7. |

The plan does not add counterpoint rules claimed for any tradition, does not turn an assumed setting into a default, and does not change what the published composer plays under its classic settings.

## Sources

The ledger holds 100 records, each with a link and a quote in `research/raw/`; `research/LEDGER.md` lists them all. Given here are the 18 records that were re-read against their source, because the code's numbers come from them, and the main sources for the traditions, the drone and the continuo, which were read once and are the weakest part of the record.

### Re-read against the source

- E-01: Smith, J.O., [Equivalent Rectangular Bandwidth](https://ccrma.stanford.edu/~jos/bbt/Equivalent_Rectangular_Bandwidth.html), in Spectral Audio Signal Processing (online book).
- E-03: Acoustics Research Institute, Austrian Academy of Sciences, [STx programmer guide, command EVAL, threshold type "hth"](https://projects.ari.oeaw.ac.at/stx/docs/wiki/index.php/Programmer_Guide/Command_Reference/EVAL/hth) (the threshold of hearing in quiet, after Terhardt).
- E-04: Seeber (2006), [posting on simultaneous masking](https://auditory.org/postings/2006/266.html), auditory.org.
- E-05: Faulkner, A. (2010), [AUDL4007 course notes "Pitch"](https://www.phon.ucl.ac.uk/courses/spsci/audper/Pitch_AUDL4007_2010.pdf), UCL.
- E-06: Micheyl, C., Delhommeau, K., Perrot, X., & Oxenham, A.J. (2006), [Influence of musical and psychoacoustical training on pitch discrimination](https://experts.umn.edu/en/publications/influence-of-musical-and-psychoacoustical-training-on-pitch-discr/), Hearing Research 219(1-2):36-47 (abstract).
- E-07: Santurette, S., Dau, T., & Oxenham, A.J. (2012), [On the possibility of a place code for the low pitch of high-frequency complex tones](https://pmc.ncbi.nlm.nih.gov/articles/PMC3528728), J Acoust Soc Am 132(6):3883-3895.
- E-08: Moore, B.C.J., Glasberg, B.R., & Peters, R.W. (1986), [Thresholds for hearing mistuned partials as separate tones in harmonic complexes](https://web.mit.edu/9.35/www/archives/2020/auditory/papers/MooreGlasbergPeters1986.pdf), J Acoust Soc Am 80(2):479-483.
- E-11: Plomp, R., & Levelt, W.J.M. (1965), [Tonal consonance and critical bandwidth](https://www.math.miami.edu/~armstrong/592sp15/Plomp_Levelt_1965.pdf), J Acoust Soc Am (the extraction did not print the journal; the volume and page are recalled).
- E-13: [Sound Modulation Metrics: Fluctuation Strength and Roughness](https://community.sw.siemens.com/articles/en_US/Knowledge/sound-modulation-metrics-fluctuation-strength-and-roughness), Siemens community knowledge article (no author printed; it cites Zwicker and Fastl).
- E-14: [Cochlea glossary](https://www.cochlea.uni-tuebingen.de/glossary.htm), University of Tuebingen.
- N-01 and N-02: Verschooten, E., Shamma, S., Oxenham, A.J., Moore, B.C.J., Joris, P.X., Heinz, M.G., & Plack, C.J. (2019), [The upper frequency limit for the use of phase locking to code temporal fine structure in humans: A compilation of viewpoints](https://par.nsf.gov/servlets/purl/10108145), Hearing Research 377.
- N-03: Semal, C., & Demany, L. (1990), [The upper limit of "musical" pitch](https://labs.sonicfield.org/library/the-upper-limit-of-musical-pitch), Music Perception (abstract).
- A-01: Huron, D. (1989), [Voice denumerability in polyphonic music of homogeneous timbres](https://labs.sonicfield.org/library/voice-denumerability-in-polyphonic-music-of-homogeneous-timbres), Music Perception (abstract).
- A-03: Brochard, R., Drake, C., Botte, M.-C., & McAdams, S. (1999), [Perceptual organization of complex auditory sequences: effect of number of simultaneous subsequences and frequency separation](https://www.mcgill.ca/mpcl/files/mpcl/brochard_2000_jephpp.pdf), J Exp Psychol Hum Percept Perform 25(6):1742-1759.
- A-05: Miller, G.A. (1956), [The magical number seven, plus or minus two](https://labs.la.utexas.edu/gilden/files/2016/04/MagicNumberSeven-Miller1956.pdf), Psychological Review 63:81-97.
- A-13: Shinn-Cunningham, B.G. (2008), [Object-based auditory and visual attention](https://www.cmu.edu/dietrich/psychology/shinn/publications/pdfs/2008/2008tics_shinn.pdf), Trends in Cognitive Sciences 12(5).
- A-15: Cowan, N. (2001), [The magical number 4 in short-term memory: a reconsideration of mental storage capacity](https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf), Behavioral and Brain Sciences 24:87-185.

### The traditions (read once, not re-read; every one is a weak source)

- M-01: Hirsch, T. (2021), [Consistency and change in the musical structure of Moroccan andalusi music studied on recordings from 1932 to 2018](https://boris.unibe.ch/184447), conference paper (abstract).
- M-02: Al-Derbi, M., & Al Matani, A. (2026), [A frequency-based comparative analysis of Arabic maqamat and the Western equal-tempered system: Interval structure and psychoacoustic implications](https://dergipark.org.tr/en/pub/rastmd/article/1932527), Rast Musicology Journal 14(2):313-349 (abstract; no numbers seen).
- M-03: Ifzarne, A., [Exploring a Quarter-Tone Tuning Based on Harmonic Series and Its Impact on Maqam Music](https://euro-acad.eu/CMS/tinymce/js/tinymce/plugins/filemanager/source/Dateien/Exploring%20a%20Quarter-Tone%20Tuning%20Based%20on%20Harmonic%20Series%20and%20Its%20Impact%20on%20Maqam%20Music%20-%20Aziz%20Ifzarne.pdf), slides.
- M-04: Serra, X., [note on Arab-Andalusian music](https://compmusic.upf.edu/index.php/kn/node/153), CompMusic project, Universitat Pompeu Fabra.
- M-05: Metioui, O., [programme note on two nubat](https://www.concertzender.nl/wp-content/uploads/2022/07/toelichting-muziek-door-omar-metioui-engels.pdf), Dutch radio, 2022.
- M-06: [Sintir](https://en.wikipedia.org/wiki/Sintir), Wikipedia.
- M-07: Abu Shumays, S. (2009), [The Fuzzy Boundaries of Intonation in Maqam: Cognitive and Linguistic Approaches](https://maqamlessons.com/analysis/media/FuzzyBoundaries_MaqamIntonation2009.pdf), Society for Ethnomusicology annual conference, abridged.
- M-08: Majeed, R. (2025), [Maqam Harmony: Compositional Techniques and Tuning Methods for Achieving Polyphony and Homophony for All Maqamat](https://jfma.journals.ekb.eg/article_443250.html), Journal of Science and Arts of Music 55(3):1602-1705 (abstract).
- S-01 and S-02: Levin, T.C., & Edgerton, M.E. (1999), [The Throat-Singers of Tuva](https://gauss.dartmouth.edu/~m5f10/Levin1999SciAm_tuvan_throat_singing.pdf), Scientific American, September 1999.
- S-03: Bloothooft, G., Bringmann, E., van Cappellen, M., van Luipen, J.B., & Thomassen, K.P., [A phonetic study of overtone singing](https://www.coli.uni-saarland.de/Phonetics/icphs/ICPhS1991/12_ICPhS_1991_Vol_5/p12.5_014.pdf), conference paper, University of Utrecht (venue and year not printed in the text).
- S-04: Utrecht University phonetics, [overtone singing page](https://audiufon.hum.uu.nl/data/e_boventoon.html).
- S-06: ["The Music of Tuva"](https://myriadartists.com/wp-content/uploads/Alash-Tuvan-Music.pdf), unattributed handout.
- S-08: Snellgrove, D.L., [Central Asian arts: Instrumental and vocal styles](https://www.britannica.com/art/Central-Asian-arts/Instrumental-and-vocal-styles), Encyclopaedia Britannica online.

### Drone and continuo

- D-02: Christensen, T., [Thoroughbass as Music Theory](https://music.arts.uci.edu/abauer/5.2/readings/Christensen,_Thoroughbass_Partimento_and_Continuo_Playing.pdf), essay, course reading copy.
- D-04: Serra, J., Koduri, G.K., Miron, M., & Serra, X. (2011), [Assessing the Tuning of Sung Indian Classical Music](https://archives.ismir.net/ismir2011/paper/000008.pdf), Proc. ISMIR 2011.
- D-05: Janakiram, V.L., & Yegnarayana, B. (1977), [Temporal variation of tonal spectrum of tambura](https://eprints.iisc.ac.in/24181/), J Acoust Soc Am 62(S1):S43 (abstract).
- D-08: Menke, Neuwirth, Hentschel, & Rohrmeier, [The Rule-of-the-Octave Hypothesis: A Quantitative Study of Tonality in Francois Couperin's Concerts](https://www.mtosmt.org/issues/mto.26.32.3/mto.26.32.3.menke_et_al.php), Music Theory Online (author list and year as returned by the fetch tool).

Where a record says "abstract", only the abstract was read.
