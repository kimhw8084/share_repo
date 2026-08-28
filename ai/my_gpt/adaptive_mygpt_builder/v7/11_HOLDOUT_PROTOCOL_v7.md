# Holdout Protocol v7

- Keep `11_PROVISIONAL_HOLDOUT_v7.csv` outside Custom GPT Knowledge.
- Do not use holdout outputs to edit the runtime before the release-candidate run is complete.
- Run each critical holdout case three times with recorded model, capabilities, Knowledge version, and raw output.
- After a holdout case materially influences a prompt change, retire it from sealed use and replace it with a fresh real or independently authored case.
- The included holdout is provisional because it was authored during this package build. Add owner-supplied real prompts that were not used during development for stronger evidence.
- Never claim holdout validation without preserved raw outputs and review.
