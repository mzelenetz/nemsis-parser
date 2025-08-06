# Run these to get started
## This is a good starting point

```bash
python ems_views.py add-view v_header        --cardinality one --section header        --use-resolved 1 --description "Header/meta"
python ems_views.py add-view v_pcr           --cardinality one --section pcr           --use-resolved 1 --description "PatientCareReport root"
python ems_views.py add-view v_emsdataset    --cardinality one --section emsdataset    --use-resolved 1 --description "Dataset constants"

python ems_views.py add-view v_dagency       --cardinality one --section dagency       --use-resolved 1 --description "Demographics agency"
python ems_views.py add-view v_agency        --cardinality one --section agency        --use-resolved 1 --description "Incident agency"

python ems_views.py add-view v_patient       --cardinality one --section patient       --use-resolved 1 --description "Patient core"
python ems_views.py add-view v_dispatch      --cardinality one --section dispatch      --use-resolved 1 --description "Dispatch"
python ems_views.py add-view v_response      --cardinality one --section response      --use-resolved 1 --description "Response"
python ems_views.py add-view v_scene         --cardinality one --section scene         --use-resolved 1 --description "Scene"
python ems_views.py add-view v_situation     --cardinality one --section situation     --use-resolved 1 --description "Primary impression/CC"
python ems_views.py add-view v_injury        --cardinality one --section injury        --use-resolved 1 --description "Injury details"
python ems_views.py add-view v_history       --cardinality one --section history       --use-resolved 1 --description "Patient history (aggregated)"
python ems_views.py add-view v_arrest        --cardinality one --section arrest        --use-resolved 1 --description "Cardiac arrest (usually single)"
python ems_views.py add-view v_disposition   --cardinality one --section disposition   --use-resolved 1 --description "Transport/disposition"
python ems_views.py add-view v_outcome       --cardinality one --section outcome       --use-resolved 1 --description "ED/hospital outcome"
python ems_views.py add-view v_payment       --cardinality one --section payment       --use-resolved 1 --description "Billing/payment"
python ems_views.py add-view v_record        --cardinality one --section record        --use-resolved 1 --description "Software/record metadata"
python ems_views.py add-view v_other         --cardinality one --section other         --use-resolved 1 --description "Other/signatures"
```
Then add the one to many tables

```bash
python ems_views.py add-view v_crew          --cardinality many --section crew          --use-resolved 1 --description "Crew members"
python ems_views.py add-view v_device        --cardinality many --section device        --use-resolved 1 --description "Devices/equipment"
python ems_views.py add-view v_protocols     --cardinality many --section protocols     --use-resolved 1 --description "Protocols applied"
python ems_views.py add-view v_labs          --cardinality many --section labs          --use-resolved 1 --description "Labs (if present)"

python ems_views.py add-view v_airway        --cardinality many --section airway        --use-resolved 1 --description "Airway attempts/groups"
python ems_views.py add-view v_exam          --cardinality many --section exam          --use-resolved 1 --description "Physical exam findings"
python ems_views.py add-view v_medications   --cardinality many --section medications   --use-resolved 1 --description "Medication administrations"
python ems_views.py add-view v_procedures    --cardinality many --section procedures    --use-resolved 1 --description "Procedures performed"
python ems_views.py add-view v_vitals        --cardinality many --section vitals        --use-resolved 1 --description "Vital sign observations"

python ems_views.py add-view v_narrative     --cardinality many --section narrative     --use-resolved 0 --description "Narratives/notes"

python ems_views.py add-view v_custom        --cardinality many --section custom        --use-resolved 1 --description "Custom config/results"
```

Finally run: 
`python ems_views.py rebuild`