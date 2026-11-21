<h1 align="center">Hi, I'm Jaydeep <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="34" alt="Waving hand"></h1>

<p align="center">
  <a href="https://jaydeep-agravat-portfolio.vercel.app/">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=61DAFB&center=true&vCenter=true&width=640&lines=React+Native+engineer+%C2%B7+New+Architecture;I+own+every+release+of+a+50K%2B+app;I+fix+bugs+in+the+libraries+you+use;Learning+German+fintech+by+building+it" alt="React Native engineer. I own every release of a 50K+ app. I fix bugs in the libraries you use. Learning German fintech by building it.">
  </a>
</p>

<p align="center">
  <a href="https://jaydeep-agravat-portfolio.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-0b0f19?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/jaydeep-agravat-0951aa334/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:jaydeepagravat94583@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Open_to-remote_or_relocation-1a9d55?style=for-the-badge" alt="Open to remote work or relocation">
</p>

---

<table>
<tr>
<td width="62%" valign="top">

### 📱 I build mobile apps people depend on

I'm a React Native engineer from Gujarat, India. I worked on **22 client apps** at an agency, and 15 of them are live.

Today I'm the **only mobile engineer** on a quick-commerce app with **50K+ downloads**. I rebuilt it from scratch and I own every release, on Android and iOS.

**💶 Right now:** learning German fintech by building in it: SEPA Instant, PSD2 and SCA, BaFin licensing, GoBD and KassenSichV, and how apps like N26 and Trade Republic are built.

</td>
<td width="38%" align="center">
<img src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif" width="100%" alt="A developer coding at two monitors">
</td>
</tr>
</table>

### 📊 The receipts

| 🚀 Releases | 🛡️ Crash-free | ⚡ JS blocking time | 💸 Google Maps bill |
| :---: | :---: | :---: | :---: |
| **11** in four months | **99.87 %** of users | **7.7 s → 0.3 s** | **₹80K → ₹25K** a month |

---

### 🧩 Open source

Fixes in React Native libraries. I read the issue, reproduce it, measure it, and keep the fix as small as the maintainer wants it.

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

<table>
<tr>
<td align="center" width="50%">
<img src="https://media.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif" width="260" alt="This is fine dog in a burning room"><br>
<sub>Me with four PRs waiting for a maintainer to approve CI</sub>
</td>
<td align="center" width="50%">
<img src="https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif" width="260" alt="Man doing mental math with equations floating around him"><br>
<sub>Me counting re-renders per product card (86 → 0)</sub>
</td>
</tr>
</table>

| | 🍿 How I pick a fix |
| :---: | --- |
| 🙅 | Guessing the fix from the issue title |
| 😎 | Reproducing it first, even on an emulator rotated 180° |
| 🙅 | "Should be faster now" |
| 😎 | **12.8 → 8.6 ms per render**, measured |
| 🙅 | A 600-line PR nobody asked for |
| 😎 | The smallest fix the maintainer agreed to |

---

### 🛠️ Things I built

<a href="https://github.com/JaydeepAgravat/zaster"><img src="https://raw.githubusercontent.com/JaydeepAgravat/zaster/main/docs/screenshots/payment-story.png" alt="A café payment in six steps, from a one-time QR code to a green till" width="100%"></a>

- 💶 **[Zaster](https://github.com/JaydeepAgravat/zaster)**: pay at a café counter phone to phone, from one bank account to another over SEPA Instant. There is no card and no fee. It has a wallet app and a till app (React Native), a web dashboard, and a Fastify + Postgres ledger. If the network drops mid-payment, the app shows *Checking* instead of guessing, so nobody is ever charged twice.
- 🧾 **[Invoice Maker](https://github.com/JaydeepAgravat/invoice-maker)**: offline invoices for tradespeople, built after reading ~110 critical app reviews. No account, no subscription: pay once. It has 384 tests and uses Kotlin Turbo Modules.
- 🎼 **[Score Reader](https://github.com/JaydeepAgravat/sheet-music-reader)**: a sheet-music reader for Android tablets. A foot-pedal page turn takes **20 ms**, because Kotlin flips the page without waiting for JavaScript.
- 🔍 **[App Teardown Handbook](https://github.com/JaydeepAgravat/app-teardown)**: how to work out the design of any mobile app without its code. I tested it on Bluesky, Expensify and Joplin: 53 conclusions were confirmed by their source code, and the 12 it got wrong are published too.

---

### 🧰 Stack

<p>
  <img src="https://skillicons.dev/icons?i=react,ts,kotlin,nodejs,postgres,githubactions,androidstudio&perline=7" alt="React, TypeScript, Kotlin, Node.js, Postgres, GitHub Actions, Android Studio">
</p>

<sub>React Native (New Architecture) · TypeScript · Kotlin · TanStack Query · Zustand · Fastify · Postgres · GitHub Actions · Fastlane</sub>

<p align="center">
  <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="180" alt="Cat typing fast on a laptop"><br>
  <sub>Me on release day</sub><br><br>
  <img src="https://komarev.com/ghpvc/?username=JaydeepAgravat&color=61dafb&style=flat-square&label=profile+views" alt="Profile views">
</p>
