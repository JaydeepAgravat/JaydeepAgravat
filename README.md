<h1 align="center">🦸 Open source log</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=61DAFB&center=true&vCenter=true&width=640&lines=Fixes+in+React+Native+libraries;Reproduce+it.+Measure+it.+Fix+it.;Keep+the+fix+as+small+as+the+maintainer+wants" alt="Fixes in React Native libraries. Reproduce it. Measure it. Fix it. Keep the fix as small as the maintainer wants.">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/merged-2-1a9d55?style=for-the-badge" alt="2 merged">
  <img src="https://img.shields.io/badge/fixed_after_my_repro-1-0b8fc9?style=for-the-badge" alt="1 fixed after my repro">
  <img src="https://img.shields.io/badge/in_review-3-d48806?style=for-the-badge" alt="3 in review">
  <img src="https://img.shields.io/badge/draft-1-7c6fd6?style=for-the-badge" alt="1 draft">
</p>

---

| | Project | What I did |
| :---: | --- | --- |
| ✅ | [**uniwind #764**](https://github.com/uni-stack/uniwind/pull/764) | Cached styles for classes with `data-*` variants: **12.8 → 8.6 ms per render, 400 → 0 re-parses**. |
| ✅ | [**react-native-keyboard-controller #1748**](https://github.com/kirillzyusko/react-native-keyboard-controller/pull/1748) | Cancels outdated CI runs on pull requests, which were wasting **~295 runner-minutes** across 300 PR runs. |
| 🐛 | [**react-native-true-sheet #1004**](https://github.com/lodev09/react-native-true-sheet/issues/1004) | A two-test repro for a Jest mock that dropped the `background` prop. Fixed the same day. |
| 👀 | [**react-native-enriched-html #858**](https://github.com/software-mansion/react-native-enriched-html/pull/858) | A `removeInvalidMentionContent` prop so mentions can't be half-edited, on iOS, Android and web. |
| 👀 | [**react-native-screens #5306**](https://github.com/software-mansion/react-native-screens/pull/5306) | Stops the Android stack header from growing by a display cutout at the bottom of the screen (**96 px** on the test device). |
| 👀 | [**Re.Pack #1532**](https://github.com/callstack/repack/pull/1532) | Source maps respect `output.devtoolModuleFilenameTemplate`, so you choose the paths in `sources`. |
| 📝 | [**react-native-audio-api #1488**](https://github.com/software-mansion/react-native-audio-api/pull/1488) | Draft: lets Android apps see when a recording is interrupted, even without audio focus. |

<sub>✅ merged · 🐛 fixed after my repro · 👀 in review · 📝 draft</sub>

---

### 🎬 The highlights, in movie scenes

<table>
<tr>
<td align="center" width="50%">
<img src="https://media.giphy.com/media/ICoxhc8wGbJ8k/giphy.gif" width="300" alt="The Flash running at super speed"><br>
<b>uniwind #764</b><br>
<sub>Components after the style cache: <b>12.8 → 8.6 ms</b> per render</sub>
</td>
<td align="center" width="50%">
<img src="https://media.giphy.com/media/yRd32T3jY8lXmL2JWc/giphy.gif" width="300" alt="Iron Man about to snap, Thanos watching"><br>
<b>keyboard-controller #1748</b><br>
<sub>A new commit lands on the PR. Every outdated CI run:</sub>
</td>
</tr>
<tr>
<td align="center" width="50%">
<img src="https://media.giphy.com/media/kbtXXtZ7TBpnXH9lTF/giphy.gif" width="300" alt="Batman saying: I'll look into it."><br>
<b>true-sheet #1004</b><br>
<sub>An issue says the Jest mock is broken. Me, before writing a two-test repro:</sub>
</td>
<td align="center" width="50%">
<img src="https://media.giphy.com/media/xT1Ra2XnbLVCNYOCCA/giphy.gif" width="300" alt="Spider-Man hanging upside down"><br>
<b>react-native-screens #5306</b><br>
<sub>Me testing a header bug with the emulator rotated 180°</sub>
</td>
</tr>
</table>

<p align="center">
  <img src="https://media.giphy.com/media/4Cpgf1zzMMy4w/giphy.gif" width="260" alt="Goku charging a Spirit Bomb"><br>
  <sub>Me with four PRs, waiting for maintainers to lend their energy (and approve CI)</sub>
</p>

---

| | 🍿 How I pick a fix |
| :---: | --- |
| 🙅 | Guessing the fix from the issue title |
| 😎 | Reproducing it first, even on an emulator rotated 180° |
| 🙅 | "Should be faster now" |
| 😎 | **12.8 → 8.6 ms per render**, measured |
| 🙅 | A 600-line PR nobody asked for |
| 😎 | The smallest fix the maintainer agreed to |
