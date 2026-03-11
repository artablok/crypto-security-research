# Trust Wallet security report: fake USDT/SOL/EURC tokens on Solana still not delisted

> Author: Arta Blockchain (artablockchain)  
> Contact: support@artablockchain.in

## 1. Summary (English)

This public report documents a **long-running security problem in Trust Wallet**.

We have repeatedly reported the following **fake / impersonation tokens on Solana** to Trust Wallet support and via GitHub pull requests. These tokens copy the branding of **USDT, SOL and EURC**, are **not** related to the real projects (Tether, Solana, Circle or us) and are actively used in **scam airdrops and phishing campaigns**.

Despite multiple tickets and PRs, the tokens below remain visible in Trust Wallet **without any spam flag or warning**, while our legitimate projects are blocked or delayed.

This creates a clear risk for users and damages the reputation of honest projects.

---

## 2. Tickets and pull requests that were closed without real action

We have:

- Created pull requests to `trustwallet/assets` to mark fake Solana mints as `status: "spam"`.
- Opened security issues and tickets with detailed lists of malicious mints.
- Received formal replies, and then our tickets were simply **closed** without removing these tokens from Trust Wallet.

Example:

- Support ticket: **#2659958** (closed without delisting the reported tokens).
- Pull request: **https://github.com/trustwallet/assets/pull/35646** – closed while the malicious mints are still tradeable and visible as normal tokens.

From our side, all technical work has been done: json-files were prepared correctly, each mint has a Solscan link and clear description that it is a fake/impersonation token.

---

## 3. List of fake tokens (Solana)

### 3.1 Fake USDT mints (SPL)

These mints impersonate **USDT** on Solana and are used in scam airdrops:

- `GCGXumhEaJoV9w4BRkC8Xw4jBGx6iv5PgrMgBd8SSD1c`
- `DMfhf8LFSXTBTwpppTMDojXgg3kcJznUmNjkta9cM1Qk`
- `9XUMSDaKnvV2FT56Wj87JLJ29x3cr6MfW6aKxZx5d9ff`
- `DNfnFTWwEwQW4R8F9Pttfp74WJnFrEHsMNQYWRbyE6CE`
- `BGtpF37rrubQoE5NnWU74KQmDf2ZvNAnafVkgxKaeGRX`

Each of these mints is **not** the official USDT mint and is used only to trick users who see “USDT” in the token name inside Trust Wallet.

### 3.2 Fake SOL / wrapped-SOL style token

- `Ag7XCgPqzrqEo7kaNjA4UXfw9buSwBQooy3uh46vfuFe` – misleading token abusing the Solana/SOL branding in the same scam campaigns.

(Additional fake EURC / other mints can be added here as the investigation continues.)

---

## 4. Why this is a problem for Trust Wallet users

- New users see the word **“USDT”**, **“SOL”** or **“EURC”** in Trust Wallet and assume it is safe and official.
- Scam airdrops send these tokens directly to wallets, so the victim thinks they “received USDT” and starts interacting with phishing sites or fake swaps.
- While honest projects are facing months of delays and rejections for listings and updates, these obvious impersonation tokens continue to exist in Trust Wallet without any spam flag.

From the point of view of user protection, this looks like:

- **Legitimate projects** – blocked, delisted, or forced to repeat paid PRs and reviews.
- **Clear scam tokens** – silently kept in the asset list and visible as normal tokens.

This situation raises questions about the consistency of Trust Wallet’s security policy.

---

## 5. Our request to Trust Wallet (escalation)

We publicly request that the Trust Wallet team:

1. **Immediately mark all mints listed in section 3 as `status: "spam"`** in `trustwallet/assets` and push the change to production.
2. Review existing support tickets and PRs that were closed without solving the problem, including:
   - Ticket **#2659958** and related conversations.
   - Pull request **#35646** and other PRs where we added these mints as spam.
3. Provide a **clear public explanation** of:
   - Why these obvious impersonation tokens were not delisted.
   - Why legitimate projects are being blocked or delayed while scam tokens remain active inside the wallet.

We are publishing this report in our own **crypto-security-research** repository to document the problem and protect the community.  
If necessary, we are ready to escalate this further to exchanges, security researchers and media who track wallet-level security issues.

---

