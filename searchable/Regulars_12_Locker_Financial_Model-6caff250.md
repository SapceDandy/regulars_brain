# Extracted text: Regulars_12_Locker_Financial_Model.xlsx

Source: [sources/library/regulars/Regulars_12_Locker_Financial_Model.xlsx](../sources/library/regulars/Regulars_12_Locker_Financial_Model.xlsx)

Extraction: XLSX cell addresses, values, and formula text; no recalculation. Source bytes remain authoritative. Layout, charts, images, and formulas may require opening the original.

## Sheet: Economics

```text
C2=Regulars 12 lockers and 48 positions
C4=MVP. Whole locker uses four positions. Shared slot uses one. USD. October 12 2026.
C6=Total bottle position capacity	D6==M16*M17
C7=Reserved positions	D7==SUMPRODUCT(D19:D22,E19:E22)
C8=Paying accounts	D8==SUM(D19:D22)
C9=Earned membership dues per month	D9==SUM(F19:F22)
C10=Month one membership collections	D10==SUM(G19:G22)
C11=Venue contribution after replaced sales	D11==D56
C12=Regulars recurring contribution	D12==D62
C13=Physical capacity check	D13==IF(D7>D6,"Over capacity","Within capacity if shared slots packed")
C16=Four customer payment groups	L16=Physical lockers	M16=12
L17=Positions per locker	M17=4
C18=Plan	D18=Accounts	E18=Slots each	F18=Earned dues/mo	G18=Month one cash	H18=Later cash/mo	I18=Bottles/mo	L18=Flat monthly venue payment	M18=500	O18=Restored MVP fee. No extra percentage fee in this draft.
C19=Whole locker monthly	D19=2	E19=4	F19==D19*$M$20/1	G19==D19*$M$20	H19==G19	I19==D19*$M$49	L19=One-time setup fee	M19=0	O19=MVP onboarding and founder installation labor included in fee.
C20=Whole locker annual	D20=1	E20=4	F20==D20*$M$21/12	G20==D20*$M$21	H20==0	I20==D20*$M$49	L20=Whole locker monthly price	M20=125	O20=Prior proposed whole-locker monthly price.
C21=Shared slot monthly	D21=12	E21=1	F21==D21*$M$22/1	G21==D21*$M$22	H21==G21	I21==D21*$M$50	L21=Whole locker annual price	M21=1000	O21=Prior whole-locker annual price. Four exclusive positions.
C22=Shared slot annual	D22=12	E22=1	F22==D22*$M$23/12	G22==D22*$M$23	H22==0	I22==D22*$M$50	L22=Shared position monthly price	M22=39	O22=Proposed monthly price. One designated bottle position.
C23=Total	D23==SUM(D19:D22)	E23==SUMPRODUCT(D19:D22,E19:E22)	F23==SUM(F19:F22)	G23==SUM(G19:G22)	H23==SUM(H19:H22)	I23==SUM(I19:I22)	L23=Shared position annual price	M23=350	O23=Lower end of prior $350-$450 shared annual proposal.
L24=Venue landed bottle cost	M24=30	O24=Replace with compliant distributor invoice.
C25=Shared slots occupy floor positions, not four short shelf tiers. Staff controls the door.	L25=Selected bottle menu price	M25=90	O25=Planning bottle price, purchased separately from membership.
C26=Annual cash is earned over twelve months. Whole accounts are not counted four times.	L26=Full service cost per bottle	M26=15	O26=Reserve labor, mixers and handling over all visits.
C27=Whole lockers available after packing shared slots	D27==M16-D19-D20-ROUNDUP((D21+D22)/M17,0)	L27=Beverage seller gross receipts tax	M27=0.067	O27=Texas beverage rate.
L28=Customer beverage tax	M28=0.0825	O28=Texas beverage rate. Pass-through.
L29=Customer dues tax assumption	M29=0.0825	O29=Unresolved tax classification. Do not bill an invented tax.
C30=Monthly venue calculation	L30=Seller reserve on membership dues	M30=0.067	O30=Conservative allowance, not a legal determination.
C31=Earned dues	D31==D9	L31=Processor percentage	M31=0.03	O31=Planning payment rate.
C32=Bottle purchases	D32==I23	L32=Fixed payment processing charge	M32=0.3	O32=One annual or monthly dues charge per account.
C33=Bottle sales	D33==D32*M25	L33=Dues refunds reserve	M33=0.02	O33=Reserve on earned dues.
C34=Total monthly revenue	D34==SUM(D31,D33)	L34=Bottle waste/refund reserve	M34=0.02	O34=Reserve beyond full bottle service cost.
L35=Existing drink sales replaced	M35=0.25	O35=25% of bottle sales replace normal-price bottle-equivalent margin.
C36=Dues seller tax reserve	D36==D31*M30	L36=Normal menu price per pour	M36=10	O36=Existing-pour comparison.
C37=Dues payment fees	D37==D31*(1+M29)*M31+(D19+D21)*M32+(D20+D22)*M32/12	L37=Saleable pours per bottle	M37=16	O37=Measured-loss allowance.
C38=Dues refund reserve	D38==D31*M33	L38=Admin cost per paying account	M38=3	O38=Venue account and ledger admin, separate from service.
C39=Account administration	D39==D8*M38	L39=Fixed cabinet upkeep monthly	M39=10	O39=MVP repair and supplies allowance.
C40=Net dues contribution	D40==D31-SUM(D36:D39)	L40=Monthly venue marketing	M40=50	O40=Editable ongoing acquisition allowance.
L41=Tax reserve on Regulars invoice	M41=0.0825	O41=Classify actual software/services invoice with accountant.
C42=Bottle product cost	D42==D32*M24	L42=Regulars support hours monthly	M42=2	O42=MVP delivery allowance.
C43=Bottle full service reserve	D43==D32*M26	L43=Regulars loaded hourly cost	M43=50	O43=Imputed founder/employee labor.
C44=Beverage seller tax	D44==D33*M27	L44=Regulars tools per month	M44=25	O44=Software and messaging allocation.
C45=Bottle payment processing	D45==D33*(1+M28)*M31+D32*M32	L45=Regulars acquisition allocation	M45=25	O45=Amortized selling cost estimate.
C46=Bottle waste/refunds	D46==D33*M34	L46=Hardware economic recovery months	M46=24	O46=Used only by the party funding hardware.
C47=Net bottle contribution	D47==D33-SUM(D42:D46)	L47=Initial venue stock in bottles	M47=15	O47=Working mix predicts fifteen purchases/month; do not automatically buy 48.
L48=One bottle planning weight in pounds	M48=3	O48=Weigh actual full SKU. Fluid volume is not full bottle weight.
C49=Existing normal-pour bottle-equivalent margin	D49==M36*M37*(1-M27-M34-M31*(1+M28))-M24-M26-M37*M32	L49=Bottles per whole account monthly	M49=1	O49=Capacity four does not imply four purchases monthly.
C50=Normal-price drink contribution replaced	D50==D32*M35*D49	L50=Bottles per shared account monthly	M50=0.5	O50=One purchase per two months for shared slot. Unverified demand.
C51=Upkeep and marketing	D51==SUM(M39:M40)
C52=Regulars fee before tax	D52==M18
C53=Regulars invoice tax reserve	D53==D52*M41	O53=Product links and legal sources checked October 12 2026
O54=https://www.ikea.com/us/en/p/kallax-shelf-unit-white-20631639/
O55=https://www.ikea.com/us/en/p/kallax-insert-with-lockable-door-white-40544274/
C56=Venue contribution after replaced sales	D56==SUM(D40,D47)-SUM(D50:D53)	O56=https://comptroller.texas.gov/taxes/mixed-beverage/faq.php
C57=Venue hardware economic recovery	D57==IF('Build budget'!F27=1,'Build budget'!F6/M46,0)
C58=Venue contribution after hardware recovery	D58==D56-D57
C60=Regulars revenue	D60==M18
C61=Regulars support tools CAC and fees	D61==M42*M43+M44+M45+D60*(1+M41)*M31+M32
C62=Regulars recurring contribution	D62==D60-D61
C63=Regulars hardware recovery	D63==IF('Build budget'!F27=2,'Build budget'!F6/M46,0)
C64=Regulars contribution after hardware recovery	D64==D62-D63
```
## Sheet: Build budget

```text
C2=Regulars MVP hardware choices
C4=Floor supported and attached to wall. Your labor is not a cash invoice in the MVP.
C5=Route 1 converted BHG 2 factory KALLAX 3 DIY	F5=2
C6=Selected landed hardware cash	F6==CHOOSE(F5,D23,F23,H23)
C7=Purchase tax assumption	F7=0.0825
C8=Item	D8=Converted BHG	F8=Factory KALLAX	H8=DIY plywood
C9=Cabinet bodies or carcass sheets	D9=96.44	F9=149.97	H9=120	L9=BHG body $96.44. Door/lock conversion is custom and unverified.
C10=Door panels or factory lock inserts	D10=35	F10=300	H10=35	L10=KALLAX: 3 x $49.99 frames and 12 x $25 factory lock inserts.
C11=Backing sheet	D11=25	F11=0	H11=25	L11=DIY: 2 x $60 carcass sheets, 1 half-inch door sheet, 1 thin back.
C12=Hinges pre-keyed locks pulls	D12=96	F12=0	H12=96
C13=Rated wall restraint allowance	D13=60	F13=60	H13=60	L13=All routes need the selected bottles trial-fitted and documented restraint details.
C14=Liners and numbered positions	D14=24	F14=24	H14=24	L14=Keep slots as labeled full-height bottle positions. No half-height shelves.
C15=Structural stiffening or bracing	D15=20	F15=0	H15=18	L15=KALLAX advertised wall-cabinet payload is 44 lb 1 oz per frame.
C16=Sealer and edge finish	D16=0	F16=0	H16=25	L16=Sixteen full bottles at 3 lb already weigh 48 lb: choose floor support.
C17=Store cutting allowance	D17=25	F17=0	H17=25
C18=Local transport allowance	D18=25	F18=25	H18=25	L18=Tools $0 assumes you own/borrow them with permission. HD rental is not free.
C19=Subtotal	D19==SUM(D9:D18)	F19==SUM(F9:F18)	H19==SUM(H9:H18)	L19=Cutting allowance is not a promise about local Home Depot free-cut policy.
C20=Estimated purchase tax on goods	D20==SUM(D9:D16)*$F$7	F20==SUM(F9:F16)*$F$7	H20==SUM(H9:H16)*$F$7
C21=Contingency	D21==SUM(D19:D20)*$F$22	F21==SUM(F19:F20)*$F$22	H21==SUM(H19:H20)*$F$22	L21=Factory locks have nonunique keys. Staff keeps keys; patrons receive no keys.
C22=Contingency rate	F22=0.1
C23=Complete landed cash cost	D23==SUM(D19:D21)	F23==SUM(F19:F21)	H23==SUM(H19:H21)
C25=Direct cabinet/parts listings; other entries are planning allowances. No hire labor in cash.	L25=https://www.walmart.com/ip/3859400021
L26=https://www.ikea.com/us/en/p/kallax-shelf-unit-white-20631639/
C27=Hardware payer 1 venue 2 Regulars	F27=1	L27=https://www.ikea.com/us/en/p/kallax-insert-with-lockable-door-white-40544274/
C28=Additional tools cash	F28=0
C29=Founder installation and assembly hours	F29=12
C30=Value per installation hour	F30=30
C31=Founder onboarding hours	F31=3
C32=Value per onboarding hour	F32=50
C33=Venue site/tax/legal review allowance	F33=250
C35=Venue hardware startup	F35==IF(F27=1,F6,0)
C36=Founder hardware startup	F36==IF(F27=2,F6,0)+F28
C37=Initial venue bottle stock	F37=='Economics'!M47*'Economics'!M24
C38=Venue startup before first monthly fee	F38==SUM(F33,F35,F37)
C39=First Regulars monthly invoice with tax reserve	F39=='Economics'!M18*(1+'Economics'!M41)
C40=Venue cash needed before dues collections	F40==SUM(F38:F39)
C41=Founder time value before monthly support	F41==F29*F30+F31*F32
C42=Founder startup cash plus time value	F42==SUM(F36,F41)
C45=Four more KALLAX lockers equals 16 positions	F45==(F9/3+F10/3+F13/3+F14/3+F18/3)*(1+F7)*(1+F22)
```
## Sheet: Launch cash

```text
C2=Mixed membership first year cash
C4=All four groups start in month one. No churn or ramp. Customer taxes excluded from revenue.
C6=Venue startup before monthly fee	D6=='Build budget'!F38
C7=Year one operating contribution	D7==SUM(F27:Q27)
C8=Ending cash after startup	D8==Q37
C9=Ending unearned annual dues	D9==Q36
C12=Annual upfront and monthly collections
F14=Month 1	G14=Month 2	H14=Month 3	I14=Month 4	J14=Month 5	K14=Month 6	L14=Month 7	M14=Month 8	N14=Month 9	O14=Month 10	P14=Month 11	Q14=Month 12
C15=Earned membership dues	F15=='Economics'!D9	G15=='Economics'!D9	H15=='Economics'!D9	I15=='Economics'!D9	J15=='Economics'!D9	K15=='Economics'!D9	L15=='Economics'!D9	M15=='Economics'!D9	N15=='Economics'!D9	O15=='Economics'!D9	P15=='Economics'!D9	Q15=='Economics'!D9
C16=Membership cash collected	F16==SUM('Economics'!G19:G22)	G16==SUM('Economics'!H19:H22)	H16==SUM('Economics'!H19:H22)	I16==SUM('Economics'!H19:H22)	J16==SUM('Economics'!H19:H22)	K16==SUM('Economics'!H19:H22)	L16==SUM('Economics'!H19:H22)	M16==SUM('Economics'!H19:H22)	N16==SUM('Economics'!H19:H22)	O16==SUM('Economics'!H19:H22)	P16==SUM('Economics'!H19:H22)	Q16==SUM('Economics'!H19:H22)
C17=Annual dues cash portion	F17==SUM('Economics'!G20,'Economics'!G22)	G17==0	H17==0	I17==0	J17==0	K17==0	L17==0	M17==0	N17==0	O17==0	P17==0	Q17==0
C18=Membership payment fees paid	F18==F16*(1+'Economics'!M29)*'Economics'!M31+(IF(0=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	G18==G16*(1+'Economics'!M29)*'Economics'!M31+(IF(1=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	H18==H16*(1+'Economics'!M29)*'Economics'!M31+(IF(2=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	I18==I16*(1+'Economics'!M29)*'Economics'!M31+(IF(3=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	J18==J16*(1+'Economics'!M29)*'Economics'!M31+(IF(4=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	K18==K16*(1+'Economics'!M29)*'Economics'!M31+(IF(5=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	L18==L16*(1+'Economics'!M29)*'Economics'!M31+(IF(6=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	M18==M16*(1+'Economics'!M29)*'Economics'!M31+(IF(7=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	N18==N16*(1+'Economics'!M29)*'Economics'!M31+(IF(8=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	O18==O16*(1+'Economics'!M29)*'Economics'!M31+(IF(9=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	P18==P16*(1+'Economics'!M29)*'Economics'!M31+(IF(10=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32	Q18==Q16*(1+'Economics'!M29)*'Economics'!M31+(IF(11=0,'Economics'!D8,'Economics'!D19+'Economics'!D21))*'Economics'!M32
C19=Membership expense recognized fees	F19=='Economics'!D37	G19=='Economics'!D37	H19=='Economics'!D37	I19=='Economics'!D37	J19=='Economics'!D37	K19=='Economics'!D37	L19=='Economics'!D37	M19=='Economics'!D37	N19=='Economics'!D37	O19=='Economics'!D37	P19=='Economics'!D37	Q19=='Economics'!D37
C20=Extra cash processing ahead of expense	F20==F18-F19	G20==G18-G19	H20==H18-H19	I20==I18-I19	J20==J18-J19	K20==K18-K19	L20==L18-L19	M20==M18-M19	N20==N18-N19	O20==O18-O19	P20==P18-P19	Q20==Q18-Q19
C22=Bottle purchases	F22=='Economics'!D32	G22=='Economics'!D32	H22=='Economics'!D32	I22=='Economics'!D32	J22=='Economics'!D32	K22=='Economics'!D32	L22=='Economics'!D32	M22=='Economics'!D32	N22=='Economics'!D32	O22=='Economics'!D32	P22=='Economics'!D32	Q22=='Economics'!D32
C23=Bottle receipts before customer tax	F23=='Economics'!D33	G23=='Economics'!D33	H23=='Economics'!D33	I23=='Economics'!D33	J23=='Economics'!D33	K23=='Economics'!D33	L23=='Economics'!D33	M23=='Economics'!D33	N23=='Economics'!D33	O23=='Economics'!D33	P23=='Economics'!D33	Q23=='Economics'!D33
C24=Venue program contribution before displacement	F24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	G24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	H24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	I24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	J24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	K24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	L24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	M24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	N24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	O24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	P24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)	Q24==SUM('Economics'!D40,'Economics'!D47)-SUM('Economics'!D51:D53)
C25=Existing drink contribution replaced	F25=='Economics'!D50	G25=='Economics'!D50	H25=='Economics'!D50	I25=='Economics'!D50	J25=='Economics'!D50	K25=='Economics'!D50	L25=='Economics'!D50	M25=='Economics'!D50	N25=='Economics'!D50	O25=='Economics'!D50	P25=='Economics'!D50	Q25=='Economics'!D50
C26=Regulars invoice total with tax reserve	F26==SUM('Economics'!D52:D53)	G26==SUM('Economics'!D52:D53)	H26==SUM('Economics'!D52:D53)	I26==SUM('Economics'!D52:D53)	J26==SUM('Economics'!D52:D53)	K26==SUM('Economics'!D52:D53)	L26==SUM('Economics'!D52:D53)	M26==SUM('Economics'!D52:D53)	N26==SUM('Economics'!D52:D53)	O26==SUM('Economics'!D52:D53)	P26==SUM('Economics'!D52:D53)	Q26==SUM('Economics'!D52:D53)
C27=Venue contribution after replaced sales	F27=='Economics'!D56	G27=='Economics'!D56	H27=='Economics'!D56	I27=='Economics'!D56	J27=='Economics'!D56	K27=='Economics'!D56	L27=='Economics'!D56	M27=='Economics'!D56	N27=='Economics'!D56	O27=='Economics'!D56	P27=='Economics'!D56	Q27=='Economics'!D56
C29=Cash change before startup	F29==F27+F16-F15-F20	G29==G27+G16-G15-G20	H29==H27+H16-H15-H20	I29==I27+I16-I15-I20	J29==J27+J16-J15-J20	K29==K27+K16-K15-K20	L29==L27+L16-L15-L20	M29==M27+M16-M15-M20	N29==N27+N16-N15-N20	O29==O27+O16-O15-O20	P29==P27+P16-P15-P20	Q29==Q27+Q16-Q15-Q20
C30=Annual upfront dues remaining unearned	F30==F36	G30==G36	H30==H36	I30==I36	J30==J36	K30==K36	L30==L36	M30==M36	N30==N36	O30==O36	P30==P36	Q30==Q36
C31=Annual dues earned this month	F31==SUM('Economics'!F20,'Economics'!F22)	G31==SUM('Economics'!F20,'Economics'!F22)	H31==SUM('Economics'!F20,'Economics'!F22)	I31==SUM('Economics'!F20,'Economics'!F22)	J31==SUM('Economics'!F20,'Economics'!F22)	K31==SUM('Economics'!F20,'Economics'!F22)	L31==SUM('Economics'!F20,'Economics'!F22)	M31==SUM('Economics'!F20,'Economics'!F22)	N31==SUM('Economics'!F20,'Economics'!F22)	O31==SUM('Economics'!F20,'Economics'!F22)	P31==SUM('Economics'!F20,'Economics'!F22)	Q31==SUM('Economics'!F20,'Economics'!F22)
C35=Beginning unearned dues	F35==0	G35==F36	H35==G36	I35==H36	J35==I36	K35==J36	L35==K36	M35==L36	N35==M36	O35==N36	P35==O36	Q35==P36
C36=Ending unearned dues	F36==F35+F17-F31	G36==G35+G17-G31	H36==H35+H17-H31	I36==I35+I17-I31	J36==J35+J17-J31	K36==K35+K17-K31	L36==L35+L17-L31	M36==M35+M17-M31	N36==N35+N17-N31	O36==O35+O17-O31	P36==P35+P17-P31	Q36==Q35+Q17-Q31
C37=Cumulative cash after startup	F37==F29-$D$6	G37==F37+G29	H37==G37+H29	I37==H37+I29	J37==I37+J29	K37==J37+K29	L37==K37+L29	M37==L37+M29	N37==M37+N29	O37==N37+O29	P37==O37+P29	Q37==P37+Q29
C39=Regulars recurring contribution	F39=='Economics'!D62	G39=='Economics'!D62	H39=='Economics'!D62	I39=='Economics'!D62	J39=='Economics'!D62	K39=='Economics'!D62	L39=='Economics'!D62	M39=='Economics'!D62	N39=='Economics'!D62	O39=='Economics'!D62	P39=='Economics'!D62	Q39=='Economics'!D62
C40=Cumulative Regulars after funding hardware	F40==F39-'Build budget'!F36	G40==F40+G39	H40==G40+H39	I40==H40+I39	J40==I40+J39	K40==J40+K39	L40==K40+L39	M40==L40+M39	N40==M40+N39	O40==N40+O39	P40==O40+P39	Q40==P40+Q39
C43=Cumulative cash subtracts hardware/review/inventory and replaced sales. Not net income.
C44=Annual dues are earned over twelve months; purchases and service must remain funded.
```
## Sheet: Site survey

```text
C2=Regulars venue installation survey
C4=Measure the selected 12-locker bank. Four bottle positions per locker; staff-only access.
C6=Venue name
C7=Street address and city
C8=TABC permit number and permit type
C10=Checks missing approval or evidence	D10==SUM(I14:I27)
C11=Installation decision	D11==IF(COUNTBLANK(D6:D8)>0,"Venue identity missing",IF(D10=0,"Review evidence and sign acceptance","Not cleared for installation"))
C13=Required check	D13=Responsible party	E13=Evidence record	F13=Status	H13=What must be confirmed
C14=Measured space and clearances	D14=Regulars and venue	F14=Pending	H14=KALLAX bank about 90.4 W x 15.4 D inches, floor supported. DIY roughly 52 W x 13 D.	I14==IF(OR(F14="Pending",F14="No",E14=""),1,0)
C15=Owner and landlord consent	D15=Venue	F15=Pending	H15=Permission to anchor, remove, repair and later expand.	I15==IF(OR(F15="Pending",F15="No",E15=""),1,0)
C16=Local permit determination	D16=Local building department	F16=Pending	H16=Actual cabinet/anchor scope exempt or required permits active.	I16==IF(OR(F16="Pending",F16="No",E16=""),1,0)
C17=Egress and fire clearance	D17=Venue and local authority	F17=Pending	H17=Exit route, signage, extinguishers, sprinkler and service access.	I17==IF(OR(F17="Pending",F17="No",E17=""),1,0)
C18=Accessibility scope reviewed	D18=Venue and RAS if needed	F18=Pending	H18=Route/service point accessible. Patron lockers if applicable.	I18==IF(OR(F18="Pending",F18="No",E18=""),1,0)
C19=Wall substrate and anchors	D19=Competent installer	F19=Pending	H19=Verified framing/masonry, manufacturer mounting points, restraint ratings and full load.	I19==IF(OR(F19="Pending",F19="No",E19=""),1,0)
C20=Utilities and rated wall checked	D20=Venue and installer	F20=Pending	H20=No utilities struck or unapproved penetrations of rated assembly.	I20==IF(OR(F20="Pending",F20="No",E20=""),1,0)
C21=TABC storage and sale structure	D21=Venue and TABC/counsel	F21=Pending	H21=Venue sourced/stamped bottles, custody, service, approved premises.	I21==IF(OR(F21="Pending",F21="No",E21=""),1,0)
C22=Dues bottle and service taxes	D22=Venue accountant	F22=Pending	H22=Actual classifications/rates confirmed before billing.	I22==IF(OR(F22="Pending",F22="No",E22=""),1,0)
C23=Lock service lawful route	D23=Venue and DPS/provider	F23=Pending	H23=Factory lock assembly or a verified pre-keyed exemption; licensed provider if required.	I23==IF(OR(F23="Pending",F23="No",E23=""),1,0)
C24=Insurance and contractor paperwork	D24=Venue and Regulars	F24=Pending	H24=Contract-required liability/property coverage and any city registration.	I24==IF(OR(F24="Pending",F24="No",E24=""),1,0)
C25=Safe service SOP and staff training	D25=Venue manager	F25=Pending	H25=ID, service refusal, bottle ledger, authorized users, incident process.	I25==IF(OR(F25="Pending",F25="No",E25=""),1,0)
C26=Paid founding mix supports economics	D26=Venue and Regulars	F26=Pending	H26=Mix supports the $500 fee and venue costs. Refund reservations before failed approval.	I26==IF(OR(F26="Pending",F26="No",E26=""),1,0)
C27=Loaded cabinet acceptance	D27=Venue and Regulars	F27=Pending	H27=Stability, doors, finish, cleanability, lock custody and labels verified.	I27==IF(OR(F27="Pending",F27="No",E27=""),1,0)
```