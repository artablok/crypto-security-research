# Arta Security Lab — Crypto Security Research

Blockchain threat intelligence from ArtaBlockchain Team: scam-token databases,
an open Security API and automated detection pipelines.

![Threat Intelligence](https://img.shields.io/badge/Threat%20Intelligence-Active-red)
![Solana Feed](https://img.shields.io/badge/Solana%20Feed-Daily-blue)

## Live threat feeds

| Feed | Scope | Update status |
|---|---|---|
| [`database/solana.json`](./database/solana.json) | Solana scam tokens | Automated, daily |
| [`database/tron.json`](./database/tron.json) | TRON scam tokens | Static dataset |
| [`database/scam_tokens.json`](./database/scam_tokens.json) | Multi-chain | Static dataset |
| [`api/index.json`](./api/index.json) | Feed index | JSON |

Feed status is tracked per feed — see the table above and the
[research log](./research-log.txt).

## Security API

Base URL:
`https://raw.githubusercontent.com/artablok/crypto-security-research/main/api/index.json`

Use cases: wallet protection, scam detection, token risk scoring, explorer warnings.

## Components

- Database updater — [`scripts/update_database.py`](./scripts/update_database.py), GitHub Actions (daily)
- Alert pipeline — [`scripts/auto_alert.py`](./scripts/auto_alert.py), [`alerts/alerts.json`](./alerts/alerts.json)
- Telegram scanner — [@ArtaSecurityScannerBot](https://t.me/ArtaSecurityScannerBot)
- Dashboard — [arta-security-dashboard](https://github.com/artablok/arta-security-dashboard)

## Ecosystem status

| Component | Status |
|---|---|
| Security API | Active |
| Threat database | Active |
| Telegram security bot | Active |
| Wallet risk scanner | In development |
| AI security engine | In development |

## Research log

Machine-readable activity log: [`research-log.txt`](./research-log.txt) (updated automatically).

## Report a scam token

Use the issue template: [Report a scam token](../../issues/new?template=report_scam_token.yml).

## Links

- Website: https://artablockchain.in
- Security page: https://artablockchain.in/security.html
- Telegram: https://t.me/ArtaBlockchain20
- Email: support@artablockchain.in

## Security

See [SECURITY.md](./SECURITY.md).
