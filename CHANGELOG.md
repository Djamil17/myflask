# CHANGELOG



## v2.0.3 (2024-04-04)

### Documentation

* docs: rearrange figures for readme ([`dde9aa8`](https://github.com/ResearchDataCom/floor-checks/commit/dde9aa85fb84c164ad00b769984cb45bd3a58e23))

* docs: explaining the architecture of the application, aws and of the cicd pipeline ([`8255605`](https://github.com/ResearchDataCom/floor-checks/commit/82556051a1a085ed576ae3b54364eb0e02f67c03))

### Fix

* fix: make sure github actions maps action variables to terraform variables ([`b5b8495`](https://github.com/ResearchDataCom/floor-checks/commit/b5b8495c10651ddd652a7d3f8dbe0814cf79e008))

### Refactor

* refactor: remove licensing comment ([`18dc5ed`](https://github.com/ResearchDataCom/floor-checks/commit/18dc5ed1ee279394474ce9111b0628d749a679b4))


## v2.0.2 (2024-04-02)

### Fix

* fix(query): too many arguments passed to floorcheck ([`0ffd6a6`](https://github.com/ResearchDataCom/floor-checks/commit/0ffd6a6c9d6f0f73f8d2133eede0e6c0a907118d))


## v2.0.1 (2024-04-01)

### Fix

* fix(test_query): include timesheet id info in test of floor check ([`21cf035`](https://github.com/ResearchDataCom/floor-checks/commit/21cf035b4cddf624d3e1b3e38ea42ee4df39b4e1))

* fix(query): repaired the floorcheck logic ([`9a5efe9`](https://github.com/ResearchDataCom/floor-checks/commit/9a5efe993124257a0a3212a1d95d92325110fd12))


## v2.0.0 (2024-03-28)

### Breaking

* ci!: remove automatic approval step ([`9b8e2f1`](https://github.com/ResearchDataCom/floor-checks/commit/9b8e2f1a3e6d2f36df4dfcbe317fd55b0416c25c))

### Unknown

* bug(infra)!: correct spelling of file in terraform plan ([`70a94da`](https://github.com/ResearchDataCom/floor-checks/commit/70a94daf16d225f345f3ddb4737213a68dc52cd3))


## v1.0.0 (2024-03-28)

### Breaking

* test(query)!: renamed test for query ([`14c7506`](https://github.com/ResearchDataCom/floor-checks/commit/14c7506cfe69779211216fc0881f5b4e815e9173))

* feat(query)!: remove test of extracting timesheet info ([`dcf90f2`](https://github.com/ResearchDataCom/floor-checks/commit/dcf90f2cb5349e81f388983d0afadde53dbd622d))

* feat(query)!: remove test of getting user response from tsheets ([`8a5bf9c`](https://github.com/ResearchDataCom/floor-checks/commit/8a5bf9c20dea9b113622f6c7a9642822c6d5d7fa))

* feat(query)!: renaming file ([`7808acb`](https://github.com/ResearchDataCom/floor-checks/commit/7808acb681953e1b51a75f49a9e28f24c2719b02))

* feat(test)!: include python unit tests for query functionality ([`9631c2b`](https://github.com/ResearchDataCom/floor-checks/commit/9631c2bfccdba3e5a825822ac699dc0cf968524b))

* feat(infra)!: parametrize terraform deployment ([`53e8a05`](https://github.com/ResearchDataCom/floor-checks/commit/53e8a054dbaad29b1978ed50404fb75913043e41))

* feat(infra)!: cron parameter ([`68188b1`](https://github.com/ResearchDataCom/floor-checks/commit/68188b180ca66e84a274b7f1d0c3dd6861686a3b))

* feat(floor_checks)!: get licensing user id ([`0a220c0`](https://github.com/ResearchDataCom/floor-checks/commit/0a220c0cacc87929bf33d0794033a32e68f91616))

* feat(packaging)!: respell gitignore text ([`08900cd`](https://github.com/ResearchDataCom/floor-checks/commit/08900cdd0c4696efccd7ed761b9353414b917691))

* feat(infra)!: creates tsheet api ssm param from local command line ([`3c3c9c1`](https://github.com/ResearchDataCom/floor-checks/commit/3c3c9c14398b315d1be3943b34e55ef33669af3d))

* feat(infra)!: store env variable of licensing user locally for ssm ([`0412fc3`](https://github.com/ResearchDataCom/floor-checks/commit/0412fc365d77615a60ab99cbca8fa73461f00fc7))

* feat(infra)!: ssm parameter for api token ([`50e6399`](https://github.com/ResearchDataCom/floor-checks/commit/50e639915c4a741c6276f90f28b9422a9ca4f056))

* feat(infra)!: lambda event permissions ([`ee12323`](https://github.com/ResearchDataCom/floor-checks/commit/ee1232354bc2ad1a3bc773e7cecd5ba6d58e5518))

* feat(packaging)!: TOKEN default removed ([`3725227`](https://github.com/ResearchDataCom/floor-checks/commit/37252275ca19bbd8a27cce74e9b0ba268e953534))

* feat(packaging)!: TOKEN requirement set in environment ([`2f11294`](https://github.com/ResearchDataCom/floor-checks/commit/2f11294b344a0de88b1bf492210efdb727d55060))

* feat!: make command to deploy lambda in aws via opentofu/terraform ([`6a0d271`](https://github.com/ResearchDataCom/floor-checks/commit/6a0d271722360dcb7ddf76e6423ec8d8b91d3d75))

* feat(lambda)!: added parameter and value to exclude licensing id ([`b8c28e9`](https://github.com/ResearchDataCom/floor-checks/commit/b8c28e9ebc705f8cc55bf6e4755d7a82c9040d41))

* feat!: add hardcoded licensing id to exclude licensing account ([`7f2c3f3`](https://github.com/ResearchDataCom/floor-checks/commit/7f2c3f3236536c363b634e841606f15f1fdf9683))

* feat(query)!: add query dictionary param, lint pass ([`59c1e36`](https://github.com/ResearchDataCom/floor-checks/commit/59c1e369179976e7f23732175cce62b5c9297710))

* feat(query)!: add query dictionary param, lint pass ([`a2e43af`](https://github.com/ResearchDataCom/floor-checks/commit/a2e43af6903279edd71220e4995af4644a9e7947))

* feat(query)!: add query dictionary param ([`363bcd6`](https://github.com/ResearchDataCom/floor-checks/commit/363bcd6fa5033a34aa9efae3b1ad000ece516435))

* refactor!: rename lambda.py to lambda_function.py ([`5de9336`](https://github.com/ResearchDataCom/floor-checks/commit/5de9336580d628b65257ce1e1b45c51844d965c1))

* feat!: redevelop as cli tool for testing locally ([`f2bcfcc`](https://github.com/ResearchDataCom/floor-checks/commit/f2bcfcceffb50328b5750b2ec85504219ddac1b0))

* feat!: create cli tool that queries/records tsheet ([`aee5cd8`](https://github.com/ResearchDataCom/floor-checks/commit/aee5cd8f2e69b0398b071a135b462ec5d33c556e))

### Build

* build(infra): record previous deployments ([`0dbf5ba`](https://github.com/ResearchDataCom/floor-checks/commit/0dbf5ba75a58f3a4fd3b49d282b81909e9938857))

* build(packaging): re-create the lambda_function.zip file when source code changes ([`e144036`](https://github.com/ResearchDataCom/floor-checks/commit/e14403617efc25fd226237494589ec4db6cf3a50))

* build(packaging): add target that packages the Lambda function ([`cbe30a6`](https://github.com/ResearchDataCom/floor-checks/commit/cbe30a62460ac0d30b88af4c9a7b1575f4811cb2))

* build: add support for Emacs/elpy development environments ([`ad26373`](https://github.com/ResearchDataCom/floor-checks/commit/ad263731fe9ddaee5d7ddf4116170fcc712f9ffa))

* build(packaging): reset to version 0.0.0 ahead of adopting semantic release ([`e5de000`](https://github.com/ResearchDataCom/floor-checks/commit/e5de000eba0116bbcd104b2d3c4b90a1ddf8e4ae))

* build: shorten test command ([`4782096`](https://github.com/ResearchDataCom/floor-checks/commit/478209647c2b562a99aa121e0012163ebbb162ad))

* build: configure the virtual environment in one target ([`5677ac3`](https://github.com/ResearchDataCom/floor-checks/commit/5677ac3f620df9f41865458f076a41d364206dde))

### Ci

* ci: store deployment state on shared storage ([`626b915`](https://github.com/ResearchDataCom/floor-checks/commit/626b915dae077b04081d519b89a4bd7beb193584))

* ci: deploy the Lambda function manually or after successful integration (main branch only) ([`bf04329`](https://github.com/ResearchDataCom/floor-checks/commit/bf0432949fd16e6b7f0d3577944ab3c4498988db))

* ci: lint code via GitHub Actions manually, at push time, or when making a pull request ([`641d7f8`](https://github.com/ResearchDataCom/floor-checks/commit/641d7f8540ae930eac61de18543c0e4c89e5e7f5))

* ci: lock OpenTofu plugin versions to make deployments repeatable ([`17f090c`](https://github.com/ResearchDataCom/floor-checks/commit/17f090c1b50fed0690a5adf691a4e605a5b22c3e))

### Documentation

* docs(infra): add figure of AWS architecture ([`69042b8`](https://github.com/ResearchDataCom/floor-checks/commit/69042b820f9347b3cc8ce094d07912eef6c771bb))

* docs(infra): explain the deployment job ([`626e3c3`](https://github.com/ResearchDataCom/floor-checks/commit/626e3c3fad65573e3670362a71e3cd58e39b4791))

* docs(infra): explain the jobs performed ([`5a5c3d0`](https://github.com/ResearchDataCom/floor-checks/commit/5a5c3d0cf1c780833bd8fa55d720b82ba5468de1))

* docs(infra): explain the continious delivery process ([`d9d97f4`](https://github.com/ResearchDataCom/floor-checks/commit/d9d97f47c143f044925be1594c4c44457b8485f9))

* docs: summarize application function ([`45f509e`](https://github.com/ResearchDataCom/floor-checks/commit/45f509e75146042fa50a483bf5143866a76ae9eb))

* docs: remove trailing whitespace ([`7e1b030`](https://github.com/ResearchDataCom/floor-checks/commit/7e1b0309a1d343ab6b8be8690abe393380088ebc))

* docs: guide future contributions to the product ([`ec78d7f`](https://github.com/ResearchDataCom/floor-checks/commit/ec78d7fef756b276dd273b6bfdffbf6a6624e4d9))

* docs: leave note to future developers regarding OIDC callback implemenetation ([`382a80c`](https://github.com/ResearchDataCom/floor-checks/commit/382a80c22a6669864eb7630ee34175580af5338e))

* docs: wrote out process of local testing ([`4eb5a20`](https://github.com/ResearchDataCom/floor-checks/commit/4eb5a2042b0438171c287930102c836bae90dc42))

### Feature

* feat(test): remove bash testing ([`d20fce7`](https://github.com/ResearchDataCom/floor-checks/commit/d20fce7f231898069acf4ee5f34509d04957477e))

* feat(packaging): enable semantic release for rdct ([`f389b7a`](https://github.com/ResearchDataCom/floor-checks/commit/f389b7a0aa90a6df99c186ad59860594d11bb839))

* feat(infra): set up environment variables for deployment environ ([`1cff7d0`](https://github.com/ResearchDataCom/floor-checks/commit/1cff7d06dfe5521fbceef75b3fd26cea86b66db9))

* feat(infra): set up environment for deployment ([`8686cdc`](https://github.com/ResearchDataCom/floor-checks/commit/8686cdcc9dd945061e86bc074d09bef30ccfae15))

* feat(infra): define a trigger for delivery ([`d9913fe`](https://github.com/ResearchDataCom/floor-checks/commit/d9913fee923ee9959389455decea0aca741119d9))

* feat(infra): add figure of AWS architecture ([`7641598`](https://github.com/ResearchDataCom/floor-checks/commit/76415987a7b8cf6be95631bb3f4f881d71540e24))

* feat(infra): add build job which deploys relevant version ([`31f5b68`](https://github.com/ResearchDataCom/floor-checks/commit/31f5b68854a3f4d19518885376c6fefdd875bf73))

* feat(infra): add testing job which deals with versioning ([`86b5f4a`](https://github.com/ResearchDataCom/floor-checks/commit/86b5f4adebd39cbdc2a07429c467c263f92f4a10))

* feat(infra): add freeze step ([`d82f8dc`](https://github.com/ResearchDataCom/floor-checks/commit/d82f8dcfbe8a776bac57ddcdfa3ab51457d1f63e))

* feat(infra): set up environment for continuous integration ([`80808ce`](https://github.com/ResearchDataCom/floor-checks/commit/80808cedc8413ce71799f8e28efa5662244ae93c))

* feat(infra): create a deploy step ([`563b6f0`](https://github.com/ResearchDataCom/floor-checks/commit/563b6f0181dcc803617ba412cdac175c4d43c883))

* feat(infra): runs packaging of code to deploy to terraform ([`cf5b10b`](https://github.com/ResearchDataCom/floor-checks/commit/cf5b10b6ac08e37a6b69a9c4b89aec2149e52baf))

* feat(infra): map terraform to github environmental variables ([`f2e3cca`](https://github.com/ResearchDataCom/floor-checks/commit/f2e3ccad4689093e44884678368a836141e5e12a))

* feat(infra): adjust default from 7 UTC to 11 UTC (7 EST) ([`3752779`](https://github.com/ResearchDataCom/floor-checks/commit/3752779e3828a95727fd621a62927890b8d65dad))

* feat(infra): run floorcheck tuesday-saturday ([`84f64a4`](https://github.com/ResearchDataCom/floor-checks/commit/84f64a414f50026f7e749a8ed5fa937e5a97a0da))

* feat(packaging): gitignore licensing id file ([`2a5818b`](https://github.com/ResearchDataCom/floor-checks/commit/2a5818bcc54114c3e19a82ed8590c1d12572c08f))

* feat(infra): extend testing time cron expression ([`bf5123c`](https://github.com/ResearchDataCom/floor-checks/commit/bf5123c811c360f42e9fb41fb4e634005495fd50))

* feat(packaging): environmental variables for lambda handler ([`d31692a`](https://github.com/ResearchDataCom/floor-checks/commit/d31692a276ecbd4eb56ca1d4f07c378528b14acc))

* feat(infra): cloud log watch ([`9511bd1`](https://github.com/ResearchDataCom/floor-checks/commit/9511bd17f821915c79482aedb293fa47b632316b))

* feat(infra): cloud log for lambda ([`a33431b`](https://github.com/ResearchDataCom/floor-checks/commit/a33431b4b4fa87b0fa0363add397d6455b6542fa))

* feat(infra): schedule report to run every 5 minutes ([`5f5529f`](https://github.com/ResearchDataCom/floor-checks/commit/5f5529f2e481f19ac1561d5c0e3fa13aa4978c25))

* feat(report): change text for message sent out ([`e8d9b61`](https://github.com/ResearchDataCom/floor-checks/commit/e8d9b61830698e2bc781c111bced8f00b97374d1))

* feat(report): remove constant variables for emails from report functionality, moved to __init__.py ([`c72fcd2`](https://github.com/ResearchDataCom/floor-checks/commit/c72fcd2a6adf0d55f85d6cdf1c17ae333c3fdd8f))

* feat(infra): deploy the Lambda function using OpenTofu ([`f4167cf`](https://github.com/ResearchDataCom/floor-checks/commit/f4167cf6e3e3739c4041112bd54dc415e0c0e8c5))

* feat(lambda): define Lambda function handler

This recapitulates the command line interface. ([`4c650e4`](https://github.com/ResearchDataCom/floor-checks/commit/4c650e4f50c3a16df2c42961b03324f0b2b5c879))

* feat(main): set defaults and add help messages for CLI ([`33c770c`](https://github.com/ResearchDataCom/floor-checks/commit/33c770c870960576dc19182afeaa2bcf966cdd62))

* feat(main): re-enable version callback ([`0dcb999`](https://github.com/ResearchDataCom/floor-checks/commit/0dcb999d27966fc047dc13ad064dc0c72e3074bd))

### Fix

* fix(lambda): use the proper Lambda function call signature

This is required even though we don&#39;t use the event or context data. ([`402c211`](https://github.com/ResearchDataCom/floor-checks/commit/402c211f54b582936604194500306ab8c376cfee))

* fix(infra): increase execution timeout

This takes at least 5 seconds to run locally, so a full minute should
be more than enough. ([`836b0b9`](https://github.com/ResearchDataCom/floor-checks/commit/836b0b961be72e85cebf43a612426a2d24d668cd))

* fix(query): add missing default value ([`ad39d25`](https://github.com/ResearchDataCom/floor-checks/commit/ad39d25707521a957c367a485161e3269897fb90))

* fix(init): add app name dunder and remove Lambda handler sketch ([`47e2b08`](https://github.com/ResearchDataCom/floor-checks/commit/47e2b08ee46c39492686bbe11186f897bf36b5f0))

* fix: add missing run-time requirement ([`f5b7999`](https://github.com/ResearchDataCom/floor-checks/commit/f5b7999e690daead9636a62aed88562aafa8e327))

### Refactor

* refactor: email message ([`83be810`](https://github.com/ResearchDataCom/floor-checks/commit/83be810230d90020dd0bdf7348813939deb83865))

* refactor: email message ([`37fc0d9`](https://github.com/ResearchDataCom/floor-checks/commit/37fc0d952cea66ff87aa16b7de45f758b7cb35c0))

* refactor(query): eliminate whitespace ([`274bcfa`](https://github.com/ResearchDataCom/floor-checks/commit/274bcfa2c51c5f46fa04d473fef552697403b07d))

* refactor(query):  change  annotations list to set ([`0f62ce3`](https://github.com/ResearchDataCom/floor-checks/commit/0f62ce3cf3e064f931d5a5ab94989e732076ba70))

* refactor(query): add annotation to control func ([`a406fd8`](https://github.com/ResearchDataCom/floor-checks/commit/a406fd875e4ab167ce734b51dad10305c52c3240))

* refactor(main): move global defaults to top-level module ([`2bb66a9`](https://github.com/ResearchDataCom/floor-checks/commit/2bb66a9f5ccdb7c75d8d20cb81d9676004596fb0))

* refactor(report): remove unused email templating code ([`3c921e2`](https://github.com/ResearchDataCom/floor-checks/commit/3c921e29b1e8e9cdb953c3d846cc45d50a5585a2))

* refactor(main): switch to relative imports ([`8b50909`](https://github.com/ResearchDataCom/floor-checks/commit/8b5090902e2e5c41dc180c7a0e9cbbc304d8d4e3))

### Unknown

* bug(query): correct logic to check failure or success ([`504257f`](https://github.com/ResearchDataCom/floor-checks/commit/504257f026a2e9febda5f07e7155e2cdea0f3ef2))

* bug(report): correct gramatical mistake in report message ([`a6fccdb`](https://github.com/ResearchDataCom/floor-checks/commit/a6fccdb6dda5f3958626332e98ce4e6bf80922bb))

* style(infra)!: format to comply with pre-commit hooks ([`8916009`](https://github.com/ResearchDataCom/floor-checks/commit/89160095094c72f4407c01e55d5b55227262ade2))

* style(infra)!: format to comply with pre-commit hooks ([`29c6443`](https://github.com/ResearchDataCom/floor-checks/commit/29c6443214357c36962e912f68521cf92b144edd))

* style(infra): add white space ([`4f582b7`](https://github.com/ResearchDataCom/floor-checks/commit/4f582b7f4a151dd393fd9a8967e1c1af277622e3))

* style(infra): add new line ([`9329fe1`](https://github.com/ResearchDataCom/floor-checks/commit/9329fe14bf4981c92f03e8a75d6d5234f3966b32))

* bug(infra): fix default time schedule ([`fec46ae`](https://github.com/ResearchDataCom/floor-checks/commit/fec46ae18a1a59d9184492e7508764c79ad88dc6))

* feat(infra)environmental variables ([`4a1146d`](https://github.com/ResearchDataCom/floor-checks/commit/4a1146d3dcfe4c70f04470920cdac1561be74677))

* feat(query)! : remove condition to check hours ([`7ffa010`](https://github.com/ResearchDataCom/floor-checks/commit/7ffa010af5ad1ecf13fb84996276c00aea82f5fb))

* revert: refactor!: rename lambda.py to lambda_function.py

This reverts commit 5de9336580d628b65257ce1e1b45c51844d965c1. ([`b3382f7`](https://github.com/ResearchDataCom/floor-checks/commit/b3382f75f3285e1890a00de494f01b957ab13845))

* style(report): wrap long lines and adjust indentation ([`1282858`](https://github.com/ResearchDataCom/floor-checks/commit/128285871de49a5e4ae35f1ec8e4a08cc1833a72))

* style(query): add whitespace, wrap long lines, and update comment syntax ([`b5b9e23`](https://github.com/ResearchDataCom/floor-checks/commit/b5b9e2332ed518f10b3b47c870a9a471fce7a86b))

* style(main): add whitespace around operators ([`97431dd`](https://github.com/ResearchDataCom/floor-checks/commit/97431ddfb0eb2f4cde05bd4d6d7dafdda1acd209))
