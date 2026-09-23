# Customer Success AI Suite

Eight interconnected apps covering the post-sale journey: **onboarding → health → sentiment → churn → expansion**.

| Stage | App | Live | Repo |
|---|---|---|---|
| Onboarding | Onboarding Journey Tracker | https://ziontechgroup.com/onboarding-journey-tracker/ | [repo](https://github.com/Zion-support/onboarding-journey-tracker) |
| Health | Customer Health Scorer | https://ziontechgroup.com/customer-health-scorer/ | [repo](https://github.com/Zion-support/customer-health-scorer) |
| Sentiment | Support Sentiment Monitor | https://ziontechgroup.com/support-sentiment-monitor/ | [repo](https://github.com/Zion-support/support-sentiment-monitor) |
| Voice | NPS Insight Engine | https://ziontechgroup.com/nps-insight-engine/ | [repo](https://github.com/Zion-support/nps-insight-engine) |
| Retention | Churn Risk Radar | https://ziontechgroup.com/churn-risk-radar/ | [repo](https://github.com/Zion-support/churn-risk-radar) |
| Expansion | Upsell Signal Scout | https://ziontechgroup.com/upsell-signal-scout/ | [repo](https://github.com/Zion-support/upsell-signal-scout) |
| VoC | Voice of Customer Hub | https://ziontechgroup.com/voice-of-customer-hub/ | [repo](https://github.com/Zion-support/voice-of-customer-hub) |
| Deflection | Support Deflection Analyzer | https://ziontechgroup.com/support-deflection-analyzer/ | [repo](https://github.com/Zion-support/support-deflection-analyzer) |

## Signal flow

`onboarding-journey-tracker` → `customer-health-scorer` ← `support-sentiment-monitor`, `nps-insight-engine` → low score → `churn-risk-radar` (save plays) · high score → `upsell-signal-scout` (expansion) · `voice-of-customer-hub` + `support-deflection-analyzer` close the loop.

## Related suites & docs

- [FIELD_SERVICES_SUITE.md](FIELD_SERVICES_SUITE.md) — field services toolchain
- [SECOPS_RELIABILITY_SUITE.md](SECOPS_RELIABILITY_SUITE.md) — SecOps & reliability pipeline
- [SALES_MARKETING_SUITE.md](SALES_MARKETING_SUITE.md) — sales & marketing AI toolchain
- Homepage spotlight: [APP_NETWORK_SPOTLIGHT_CUSTOMER_SUCCESS.md](https://github.com/Zion-support/zion-support.github.io/blob/main/APP_NETWORK_SPOTLIGHT_CUSTOMER_SUCCESS.md)

---
🗂️ [Zion App Network — Master Directory](../README.md) · https://ziontechgroup.com/ · Plans: https://ziontechgroup.com/en/plans/ · Discovery: https://ziontechgroup.com/discovery/
