# Extracted text: Regulars_Pricing_and_MVP_Plan.xlsx

Source: [sources/library/regulars/Regulars_Pricing_and_MVP_Plan.xlsx](../sources/library/regulars/Regulars_Pricing_and_MVP_Plan.xlsx)

Extraction: XLSX cell addresses, values, and formula text; no recalculation. Source bytes remain authoritative. Layout, charts, images, and formulas may require opening the original.

## Sheet: Venue model

```text
A2=Regulars venue economics
A3=Monthly steady-state estimates. USD. Replace costs and behavior assumptions before quoting.
A5=Monthly result	B5=Amount	D5=Lockers	E5=Revenue	F5=Program contribution	G5=Additional contribution	H5=Regulars fee
A6=Occupied lockers	B6==B24	D6=20	E6==D6*($B$25+$B$26*'Bottle pricing'!$B$36)	F6==D6*$B$62-H6*(1+$B$45)-$B$68	G6==D6*$B$63-H6*(1+$B$45)-$B$68-$B$36	H6==MAX($B$27,D6*$B$25*$B$28)
A7=Dues per locker	B7==B25	D7=40	E7==D7*($B$25+$B$26*'Bottle pricing'!$B$36)	F7==D7*$B$62-H7*(1+$B$45)-$B$68	G7==D7*$B$63-H7*(1+$B$45)-$B$68-$B$36	H7==MAX($B$27,D7*$B$25*$B$28)
A8=Dues and bottle revenue, before sales tax	B8==B65	D8=60	E8==D8*($B$25+$B$26*'Bottle pricing'!$B$36)	F8==D8*$B$62-H8*(1+$B$45)-$B$68	G8==D8*$B$63-H8*(1+$B$45)-$B$68-$B$36	H8==MAX($B$27,D8*$B$25*$B$28)
A9=Program contribution before displacement	B9==B69
A10=Existing drink contribution displaced	B10==B70	D10=Same per-locker assumptions at each size. These are not demand forecasts.
A11=Seat contribution displaced	B11==B71
A12=Estimated additional venue contribution	B12==B72	D12=Additional contribution subtracts sales that the program replaces.
D13=Default: 25% of program bottles replace a full-price bottle-equivalent purchase.
A14=Regulars monthly fee revenue	B14==B76
A15=Regulars contribution after delivery costs	B15==B81	D15=Membership tax treatment is unresolved; conservative reserves are included.
D16=Customer taxes are pass-through collections, not venue revenue.
A17=Installation and setup outlay	B17==SUM(B73:B74)
A18=Month one after full installation / setup	B18==B75	D18=Installation is a $200-per-locker estimate, not a vendor quote.
D19=Month-one estimate assumes every modeled locker is occupied for the full month.
A20=Contribution is before existing rent, general overhead, financing and income tax.	D20=A slower ramp and working-capital needs can make the launch more expensive.
A21=Includes estimated future bottle service and fixture cost recovery.
A23=Editable assumptions	D23=Blue numbers in amber cells are editable. Sources and definitions are beside each input.
A24=Occupied, paying lockers	B24=40	D24=One paid account per locker. Check physical and service capacity.
A25=Monthly VIP locker dues	B25=49	D25=Proposed test price; bottles are purchased separately.
A26=Bottles purchased per locker / month	B26=1	D26=Unverified behavior. Test 0.5 and 1.0; purchases can be consumed over many visits.
A27=Regulars minimum monthly software fee	B27=249	D27=Proposed standard fee; exclude installation and media buying.
A28=Regulars share of dues	B28=0.1	D28=Fee is the greater of the minimum or this share; no bottle commission.
A29=Customer tax on membership dues	B29=0.0825	D29=Planning assumption pending classification; collected on top of dues.
A30=Venue tax reserve on membership dues	B30=0.067	D30=Conservative allowance, NOT a determination that 6.7% applies to dues.
A31=Venue administration cost / locker	B31=3	D31=Monthly check-in and account administration; excludes bottle service.
A32=Installed fixture cost / locker	B32=200	D32=Unverified hardware + installation allowance; use zero only for sunk usable fixtures.
A33=Fixture cost recovery period, months	B33=36	D33=Economic recovery allowance, not an accounting depreciation opinion.
A34=Fixed monthly upkeep	B34=50	D34=Repair and program supplies allowance.
A35=Fixed monthly program marketing	B35=100	D35=Venue-funded program acquisition allowance; replace with actual cost.
A36=Monthly displaced-seat contribution	B36=100	D36=Estimated contribution lost when seats replace other paying guests.
A37=Existing drink sales displaced, equivalent share	B37=0.25	D37=0.25 means 4 program bottles replace 1 full-price bottle-equivalent purchase.
A38=Verified extra food / guest contribution per locker	B38=0	D38=Only incremental margin after all associated costs. Zero avoids assuming an uplift.
A39=Rowdy monthly locker dues, if verified	D39=Enter current total annual dues / 12, or actual monthly dues. Unknown is not zero.
A40=One-time Regulars setup fee	B40=500	D40=Proposed price. Fixtures are additional; no annual prepayment assumed.
A41=Regulars support hours / venue / month	B41=2	D41=Founder delivery effort allowance; excludes one-time onboarding.
A42=Regulars loaded hourly delivery cost	B42=50	D42=Imputed founder/staff cost, not an assertion of actual cash payroll.
A43=Regulars tools / venue / month	B43=25	D43=Hosting, messaging and administration allocation.
A44=Regulars selling-cost allocation / month	B44=25	D44=Illustrative amortized acquisition expense. Replace with measured CAC.
A45=Tax reserve on Regulars invoice	B45=0.0825	D45=Conservative customer-tax assumption, pending service tax classification.
A46=Membership refund reserve	B46=0.02	D46=Reserve based on pre-tax dues; do not treat cancellation refunds as profit.
A54=Unit and monthly calculations
D55=Scope and source notes
A56=Net dues contribution / locker	B56==B25*(1-B30-B46-'Bottle pricing'!B31*(1+B29))-'Bottle pricing'!B32
A57=Bottle contribution / locker	B57==B26*'Bottle pricing'!B48	D57=This models venue-sourced bottle sales under an approved permit-specific structure.
A58=Additional food / guest contribution / locker	B58==B38	D58=Private-club locker systems have separate rules; they are not blanket authorization for bars.
A59=Administration / locker	B59==B31	D59=TABC permit guidance, accessed October 1, 2026:
A60=Fixture cost recovery / locker	B60==B32/B33	D60=TABC Mixed Beverage Permit guide. Full source URL is in row 84.
A61=Existing drink contribution displaced / locker	B61==B26*B37*'Bottle pricing'!B51
A62=Unit contribution before displacement	B62==SUM(B56:B58)-SUM(B59:B60)	D62=Private club statute: https://tcss.legis.texas.gov/resources/AL/htm/AL.32.htm
A63=Unit contribution after drink displacement	B63==B62-B61
D64=Taxes on dues and software require venue-specific classification. Reserves are assumptions.
A65=Monthly dues and bottle revenue	B65==B24*(B25+B26*'Bottle pricing'!B36)	D65=Fixture recovery spreads installation cost; the initial cash outlay is shown separately.
A66=Regulars fee before invoice tax	B66==MAX(B27,B24*B25*B28)
A67=Tax reserve on Regulars invoice	B67==B66*B45	D67=All purchase frequency, displacement, service and installation costs are unverified estimates.
A68=Fixed upkeep and marketing	B68==SUM(B34:B35)	D68=No lift in food, guest purchases, seat sales or lower-tier membership dues is assumed.
A69=Program contribution before displacement	B69==B24*B62-SUM(B66:B68)
A70=Existing drink contribution displaced	B70==B24*B61	D70=Compare existing customers before/after and invited/uninvited cohorts where practical.
A71=Existing seat contribution displaced	B71==B36	D71=Before/after differences are directional evidence, not causal proof.
A72=Estimated additional venue contribution	B72==B69-SUM(B70:B71)
A73=Full installed fixture cost	B73==B24*B32	D73=At zero paid lockers the software minimum, fixed costs and seat allowance remain.
A74=One-time setup cost	B74==B40	D74=Cancel or adjust commitments when the actual operating agreement permits.
A75=Month one after installation and setup	B75==B72+B24*B60-SUM(B73:B74)
A76=Regulars monthly fee revenue	B76==B66	D76=Platform contribution excludes development, general overhead and income tax.
A77=Regulars delivery cost	B77==B41*B42
A78=Regulars tools allocation	B78==B43
A79=Regulars selling-cost allocation	B79==B44
A80=Regulars invoice processing	B80==B76*(1+B45)*'Bottle pricing'!B31+'Bottle pricing'!B32
A81=Regulars contribution before general overhead	B81==B76-SUM(B77:B80)
A84=https://www.tabc.texas.gov/static/sites/default/files/2021-08/mixed-beverage-permit-mb-on-premise-retailers-lc.pdf
```
## Sheet: Bottle pricing

```text
A2=Regulars bottle pricing
A3=USD. Planning assumptions as of October 1, 2026. Prices exclude customer tax and tips.
A5=Per-bottle result	B5=Amount	D5=Bottle price	E5=Retail multiple	F5=Direct contribution	G5=Margin	H5=Volume vs 4×
A6=Selected menu price	B6==B36	D6==$B$24*E6	E6=2	F6==D6*$B$42-$B$43	G6==F6/D6	H6==IF(F6>0,$B$54/F6,"n.a.")
A7=Actual landed bottle cost	B7==B25	D7==$B$24*E7	E7=2.5	F7==D7*$B$42-$B$43	G7==F7/D7	H7==IF(F7>0,$B$54/F7,"n.a.")
A8=Direct contribution after variable costs	B8==B48	D8==$B$24*E8	E8=3	F8==D8*$B$42-$B$43	G8==F8/D8	H8==IF(F8>0,$B$54/F8,"n.a.")
A9=Price needed for target contribution	B9==B53	D9==$B$24*E9	E9=4	F9==D9*$B$42-$B$43	G9==F9/D9	H9==IF(F9>0,$B$54/F9,"n.a.")
A10=Direct contribution margin	B10==B49
D11=Volume needed to equal 4× bottle contribution; excludes membership dues.
A12=Direct contribution excludes dues, venue fixed costs, and lost existing drink sales.	D12=The 4× retail benchmark is user-reported, not independently verified.
A13=Reserve the full expected service cost, even when a bottle is consumed over several visits.
A14=Do not treat upfront bottle receipts as immediate net profit.
A17=Customer cost, including locker dues	D17=Bottles / month	E17=Monthly total	F17=Cost / bottle	G17=Rowdy total	H17=Savings
D18=0.5	E18=='Venue model'!$B$25+D18*$B$36	F18==E18/D18	G18==IF(ISNUMBER('Venue model'!$B$39),'Venue model'!$B$39+D18*$B$24*$B$37,"n.a.")	H18==IF(ISNUMBER(G18),G18-E18,"n.a.")
A19=Rowdy comparison needs its actual locker dues.	D19=1	E19=='Venue model'!$B$25+D19*$B$36	F19==E19/D19	G19==IF(ISNUMBER('Venue model'!$B$39),'Venue model'!$B$39+D19*$B$24*$B$37,"n.a.")	H19==IF(ISNUMBER(G19),G19-E19,"n.a.")
A20=A cheaper bottle does not guarantee a cheaper total membership.	D20=2	E20=='Venue model'!$B$25+D20*$B$36	F20==E20/D20	G20==IF(ISNUMBER('Venue model'!$B$39),'Venue model'!$B$39+D20*$B$24*$B$37,"n.a.")	H20==IF(ISNUMBER(G20),G20-E20,"n.a.")
A22=Editable assumptions	D22=Blue numbers in amber cells are editable. All commercial costs are estimates.
A24=Retail shelf price used for comparison	B24=30	D24=Illustrative retail price; obtain the same SKU and size.
A25=Venue landed cost per bottle	B25=30	D25=Replace with a compliant distributor invoice; not the retail shelf price.
A26=Saleable servings per 750 ml bottle	B26=16	D26=Illustrative 1.5 oz servings after allowance for loss. Use measured yield.
A27=Existing menu price per serving	B27=10	D27=Illustrative normal pour price used only for displacement analysis.
A28=Full service cost per bottle	B28=15	D28=Labor, ice, basic mixers, glasswashing and handling across all visits.
A29=Mixed beverage gross receipts tax	B29=0.067	D29=Texas rate; venue bears this tax on applicable beverage receipts.
A30=Customer mixed beverage sales tax	B30=0.0825	D30=Collected on top of menu price; not counted as venue revenue.
A31=Processor percentage	B31=0.03	D31=Planning estimate, applied to the charge including customer tax.
A32=Processor fixed fee per transaction	B32=0.3	D32=One bottle transaction assumed. Tips are outside this model.
A33=Bottle refunds / waste reserve	B33=0.02	D33=Extra reserve based on pre-tax price. Replace with measured results.
A34=Target direct contribution per bottle	B34=30	D34=Planning target, before dues, fixed costs and displacement.
A35=Menu price rounding increment	B35=5	D35=Round the calculated floor upward to this price increment.
A36=Selected bottle menu price	B36=90	D36=Recommended starting test price for this illustrative cost structure.
A37=Rowdy reported retail-price multiple	B37=4	D37=User report on October 1, 2026; current bottle menu not verified.
A40=Calculation detail	D40=Sources and assumptions
A42=Price retained after percentage costs	B42==1-B29-B31*(1+B30)-B33	D42=Tax source: Texas Comptroller, Mixed Beverage Taxes FAQ, accessed October 1, 2026.
A43=Bottle, service and fixed transaction costs	B43==SUM(B25,B28,B32)	D43=https://comptroller.texas.gov/taxes/mixed-beverage/faq.php
D45=Rowdy public page confirms its locker program but does not publish these prices.
D46=https://www.rowdycowboy.com/blog/whiskey-locker-north-texas/
A48=Selected bottle direct contribution	B48==B36*B42-B43	D48=All other inputs are proposed planning assumptions, not venue quotes or forecasts.
A49=Selected bottle contribution margin	B49==B48/B36	D49=The same cost assumptions are used for the existing-pour comparison.
A50=Existing full-price bottle-equivalent sales	B50==B26*B27	D50=Actual transaction counts and service costs may differ for individual drink sales.
A51=Existing full-price equivalent contribution	B51==B50*B42-B43
A52=Unrounded menu-price floor	B52==(B34+B43)/B42
A53=Rounded menu-price floor	B53==ROUNDUP(B52/B35,0)*B35
A54=4× benchmark bottle contribution	B54==B24*B37*B42-B43
```
## Sheet: MVP plan

```text
A2=KUDJO and Regulars pilot plan
A3=Proposed gates are planning targets, not industry benchmarks. October 1, 2026.
A5=Product	B5=Component	C5=Minimum build or operating process	D5=What it must prove
A6=KUDJO	B6=Pilot scope	C6=One Austin-area service category. Start with three detailing businesses and two clearly identified KUDJO AI presenters. Run a 45-day sales pilot.	D6=New customers will book real services through KUDJO-owned marketing. AI characters do not bring an audience automatically.
A7=KUDJO	B7=Content workflow	C7=Use approved real business footage and real before/after work. Add the virtual presenter and track each post. Label the AI presenter and commercial relationship in the content.	D7=Test persuasive presentation without inventing customer visits, opinions, results or testimonials.
A8=KUDJO	B8=Customer flow	C8=Tagged video link → a specific real service, scope and price → merchant booking → completed appointment → verified payment and refund record.	D8=Measure completed, paid, new-customer appointments rather than views, clicks or unfulfilled reservations.
A9=KUDJO	B9=Merchant tools	C9=One mobile page per merchant, tagged links, booking connection, completion/refund queue and a weekly invoice/report. Existing payment and scheduling tools are sufficient.	D9=The merchant can verify every fee. The MVP does not need universal POS matching.
A10=KUDJO	B10=Commercial test	C10=Propose 20% of the first completed, paid, pre-tax service; no repeat commission during the pilot. KUDJO funds a capped test media budget and records production labor.	D10=At a $150 service, the fee is $30. Media, AI, production, support, billing and refunds must fit below that fee for positive contribution.
A11=KUDJO	B11=Creative comparison	C11=Compare AI-presenter and business-footage-only ads with the same offer, footage, geography and budget using an ad experiment. Report organic performance separately.	D11=Determine whether the AI presenter improves acquisition economics. Record real cost per completed booking.
A12=KUDJO	B12=Continue criteria	C12=Target 30 verified new-customer paid bookings, positive acquisition contribution, and at least two of three merchants paying an invoice and choosing to continue.	D12=These are commercial learning gates. A small trial does not establish statistically reliable superiority of the AI creative.
A13=Regulars	B13=Pilot scope	C13=One permitted venue, 20 VIP locker accounts, a small lower membership cohort and free guest accounts. Run 60 days with monthly renewal.	D13=Customers pay, return, use benefits, and renew; the bar can deliver the experience consistently.
A14=Regulars	B14=Guest-to-VIP flow	C14=Free guest pass; proposed $19/month membership with recognition and earlier access to limited bookings; proposed $49/month VIP including one locker. Bottles separate.	D14=Test upgrades across the intended hierarchy: guest → member → locker VIP. The financial model counts locker dues only.
A15=Regulars	B15=Locker and bottle ledger	C15=Staff QR lookup, current membership, locker assignment, bottle SKU/size, purchase receipt, estimated remaining servings and an audit trail. Bar retains custody and serves.	D15=Accurate inventory and fast, repeatable service. A balance estimate is not permission to serve or proof of exact volume.
A16=Regulars	B16=Seat experience	C16=Publish six marked reservable stools for selected events and one quiet evening. Use exact seat/time inventory and a 15-minute arrival grace period. Game entry remains free.	D16=A confirmed booking is honored without double-booking. Membership gives priority within available inventory.
A17=Regulars	B17=Visit activation	C17=Run one weekly quiet-evening invitation. Track opt-in source, member arrival, guest count, upgrades and matched receipts; use a comparison group where feasible.	D17=Learn whether the program creates additional visits and spend. Separate existing customers and already-planned visits.
A18=Regulars	B18=Owner report	C18=Show paid accounts, repeat visits, due-for-renewal cohort, verified sales, bottle service obligations, costs, lost existing margin and Regulars fees. Match each receipt once.	D18=Demonstrate additional venue contribution and feasible staff effort. Gross program sales alone are insufficient.
A19=Regulars	B19=Continue criteria	C19=Target 20 paid lockers, at least 50% returning within 30 days, at least 70% renewal among eligible accounts, 90% receipt matching and positive additional contribution.	D19=Use real costs and recorded behavior to replace the spreadsheet assumptions before expanding.
A20=Regulars	B20=Permit and pricing gate	C20=Venue verifies its permit, ownership/custody/service model, allowed bottle pricing, guest rules and the tax treatment of dues and service fees before taking program payments.	D20=The commercial model is not a legal determination. Private-club rules do not automatically apply to an ordinary bar.
A21=Both	B21=Expansion evidence	C21=Keep universal identity matching, camera presence, automated TV/music control and a cross-venue credit market for later tests. Credits need a separate legal and redemption-economics pilot.	D21=This MVP validates acquisition, retention and hospitality operations. It does not yet validate the wholesale-credit resale model.
```