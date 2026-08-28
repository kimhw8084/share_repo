# 01_SETUP_AND_TEST_GUIDE.md

## Upload set

Upload this file set into the GPT Knowledge area:

1. `00_VISUAL_SYSTEM_LAW_v4_GOLDEN.md`
2. `01_character_lineup`
3. `02_character_poses`
4. `03_visual_style_guide`
5. `04_mina_reference`
6. `05_tomo_reference`
7. `06_toto_reference`
8. `07_momo_reference`
9. `08_bugu_reference`
10. `09_chai_reference`
11. `10_professor_sori_reference`
12. `11_template_whole_story`
13. `12_template_main_characters`
14. `13_template_plot_mechanism`
15. `14_template_real_world`
16. `15_template_trouble`
17. `16_template_expert_lens`
18. `17_template_future_path`

If your GPT builder has a file-count limit, prioritize:

1. `00_VISUAL_SYSTEM_LAW_v4_GOLDEN.md`
2. `01_character_lineup`
3. `02_character_poses`
4. `03_visual_style_guide`
5. a character contact sheet
6. a template contact sheet

## Paste into GPT instruction box

Use the content from `GPT_BUILDER_INSTRUCTIONS.txt`.

## First test prompt

Use this to verify the GPT is reading the law file:

"Before generating anything, list the active Knowledge references you would use for the topic: AI CLI tools, agents, and skills. Then give the image-pack plan only."

## Character lock test

Use:

"Do not generate yet. Create the Character Lock Block for Image 1 of the topic: AI CLI tools, agents, and skills."

Pass criteria:
- names the correct character refs
- states Character Mode
- says no generic substitute
- says no childification
- says character names must not appear on final image

## Numbering test

Use:

"Do not generate. Give the numbering plan for Whole Story Image 1. Make sure no duplicate numbers."

Pass criteria:
- max 5 zones
- unique sequential numbering or no numbering
- no repeated number badges
