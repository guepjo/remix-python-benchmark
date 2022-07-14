def get_medium_payload():
    return {
    "host_": "ltx1-app3767.stg.example.com",
    "count": 25,
    "page": {
        "page_size": 25,
        "total_records": 95,
        "total_pages": 4,
        "current_page": 1
    },
    "data": [
        {
            "cm_id": 589,
            "created": "Wed, 06 Jul 2022 09:18:43 UTC",
            "updated": "Wed, 06 Jul 2022 09:18:43 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "a12f1b94-fd0c-11ec-abee-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "lor1-app37074.prod.example.com",
            "inops_data": {
                "device_id": 871036,
                "state": "Production",
                "fabric": "prod-lor1",
                "fabric_group": "prod",
                "site": "LOR1",
                "cage": "B",
                "cabinet": "817",
                "ru": 14,
                "environment": "PROD",
                "warranty_start": 1529910000,
                "warranty_expiration": 1624604400,
                "location": "LOR1:B:817:14",
                "created_time": 1531782222,
                "template_name": "SM-DENSE-031",
                "template_group": "App node, 256G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "followfeed-models",
                    "followfeed-storage"
                ],
                "services": [
                    "followfeed-models",
                    "followfeed-storage"
                ]
            },
            "apps": [
                "followfeed-models",
                "followfeed-storage"
            ],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "softwareraid"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "softwareraid",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.prod.example.com/prod-lor1/api/v2/hosts/lor1-app37074.prod.example.com?show_checks=true&show_extra=true",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "mdadm has detected a degraded array. A major disk failure has occurred, data loss is possible, replace disk now.",
                    "is_manual": False,
                    "component": "",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 06 Jul 2022 09:18:43 UTC",
                    "updated": "Wed, 06 Jul 2022 09:18:43 UTC"
                }
            ]
        },
        {
            "cm_id": 587,
            "created": "Tue, 28 Jun 2022 07:00:50 UTC",
            "updated": "Mon, 11 Jul 2022 17:22:38 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "0a6682c2-f6b0-11ec-809c-ac1f6bd50e76",
            "status": "HKE_FORWARDER_ERROR",
            "hostname": "lor1-app13105.prod.example.com",
            "inops_data": {
                "device_id": 429804,
                "state": "Production",
                "fabric": "prod-lor1",
                "fabric_group": "prod",
                "site": "LOR1",
                "cage": "A",
                "cabinet": "905",
                "ru": 22,
                "environment": "PROD",
                "warranty_start": 1463122800,
                "warranty_expiration": 1557730800,
                "location": "LOR1:A:905:22",
                "created_time": 1466639081,
                "template_name": "SM-DENSE-020",
                "template_group": "App node, 64G",
                "model": "Fat Twin Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "espresso"
                ],
                "services": [
                    "espresso-storage-node"
                ]
            },
            "apps": [
                "espresso-storage-node"
            ],
            "app_owners": [
                "espresso-sre@linkedin.com"
            ],
            "actionable": "no",
            "workflow_state": "Pending Approvals",
            "hooks_phase_name": "PRE",
            "hooks_phase_status": "",
            "hooks_enabled": True,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "Test CM for HE testing.",
                    "is_manual": True,
                    "component": "Test CM for HE",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Tue, 28 Jun 2022 07:00:50 UTC",
                    "updated": "Tue, 28 Jun 2022 07:00:50 UTC"
                }
            ]
        },
        {
            "cm_id": 586,
            "created": "Tue, 28 Jun 2022 05:59:13 UTC",
            "updated": "Mon, 11 Jul 2022 17:22:38 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "6ef90f38-f6a7-11ec-a632-ac1f6bd50e76",
            "status": "HKE_FORWARDER_ERROR",
            "hostname": "lor1-app12395.prod.example.com",
            "inops_data": {
                "device_id": 434101,
                "state": "Production",
                "fabric": "prod-lor1",
                "fabric_group": "prod",
                "site": "LOR1",
                "cage": "A",
                "cabinet": "813",
                "ru": 49,
                "environment": "PROD",
                "warranty_start": 1463122800,
                "warranty_expiration": 1557730800,
                "location": "LOR1:A:813:49",
                "created_time": 1466639605,
                "template_name": "SM-DENSE-020",
                "template_group": "App node, 64G",
                "model": "Fat Twin Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "espresso"
                ],
                "services": [
                    "espresso-storage-node"
                ]
            },
            "apps": [
                "espresso-storage-node"
            ],
            "app_owners": [
                "espresso-sre@linkedin.com"
            ],
            "actionable": "no",
            "workflow_state": "Pending Approvals",
            "hooks_phase_name": "POST",
            "hooks_phase_status": "",
            "hooks_enabled": True,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "This is test CM.",
                    "is_manual": True,
                    "component": "Test CM for hooks engine integration/",
                    "jira_ticket": "DCTECHS-204546",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204546",
                    "created": "Tue, 28 Jun 2022 05:59:13 UTC",
                    "updated": "Tue, 28 Jun 2022 06:11:14 UTC"
                }
            ]
        },
        {
            "cm_id": 579,
            "created": "Wed, 15 Jun 2022 14:04:00 UTC",
            "updated": "Thu, 23 Jun 2022 05:04:44 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "00f44b12-ecb4-11ec-8702-ac1f6bd4b988",
            "status": "FINISHED_PLAN_EXECUTION",
            "hostname": "lor1-0001446.int.example.com",
            "inops_data": {
                "device_id": 538861,
                "state": "Production",
                "fabric": "ei4",
                "fabric_group": "ei",
                "site": "LOR1",
                "cage": "B",
                "cabinet": "1403",
                "ru": 9,
                "environment": "STG",
                "warranty_start": 1493967600,
                "warranty_expiration": 1588575600,
                "location": "LOR1:B:1403:9",
                "created_time": 1494438978,
                "template_name": "SM-DENSE-020",
                "template_group": "App node, 64G",
                "model": "Fat Twin Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "storops-sds-nvmesh"
                ],
                "services": [
                    "storops-sds-nvmesh"
                ]
            },
            "apps": [
                "storops-sds-nvmesh"
            ],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Resolve Fault",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "smart_enabled"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "smart_enabled",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei4/api/v2/hosts/lor1-0001446.int.example.com?show_checks=true&show_extra=true",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "SMARTD has detected a drive that is failing.  This drive has passed thresholds for health checks.  When the drive fails or is replaced, the RAID array will have to perform data reconstruction, which is an expensive I/O process and can effect production applications. The SMARTD should have been enabled on this host but it is not.",
                    "is_manual": False,
                    "component": "SMART disabled on: {'sdb'}",
                    "jira_ticket": "DCTECHS-204537",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204537",
                    "created": "Wed, 15 Jun 2022 14:04:00 UTC",
                    "updated": "Thu, 23 Jun 2022 05:04:46 UTC"
                }
            ]
        },
        {
            "cm_id": 578,
            "created": "Wed, 15 Jun 2022 13:26:45 UTC",
            "updated": "Wed, 15 Jun 2022 13:26:47 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "cc63998e-ecae-11ec-ac84-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "lor1-0003193.int.example.com",
            "inops_data": {
                "device_id": 1643232,
                "state": "Production",
                "fabric": "ei4",
                "fabric_group": "ei",
                "site": "LOR1",
                "cage": "C",
                "cabinet": "115",
                "ru": 1,
                "environment": "STG",
                "warranty_start": 1597215600,
                "warranty_expiration": 1691996400,
                "location": "LOR1:C:115:1",
                "created_time": 1597692786,
                "template_name": "DELL-STOR-032-SSD",
                "template_group": "Storage node",
                "model": "R740XD",
                "manufacturer": "Dell",
                "multiproducts": [
                    "northguard",
                    "kmon-agent"
                ],
                "services": [
                    "northguard",
                    "kmon-agent"
                ]
            },
            "apps": [
                "northguard",
                "kmon-agent"
            ],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "perc_tooling",
                "perc_slot_state"
            ],
            "total_faults": 2,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "perc_tooling",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei4/api/v2/hosts/lor1-0003193.int.example.com?show_checks=true&show_extra=true",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "Error in Running perccli64",
                    "is_manual": False,
                    "component": "ex: Cannot allocate memory for a fork!",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 15 Jun 2022 13:26:45 UTC",
                    "updated": "Wed, 15 Jun 2022 13:26:45 UTC"
                },
                {
                    "created_by": "Nurse",
                    "check_id": "perc_slot_state",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei4/api/v2/hosts/lor1-0003193.int.example.com?show_checks=true&show_extra=true",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "Bad state of one or more Physical Slots",
                    "is_manual": False,
                    "component": "Could not collect slots due to tooling error",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 15 Jun 2022 13:26:46 UTC",
                    "updated": "Wed, 15 Jun 2022 13:26:46 UTC"
                }
            ]
        },
        {
            "cm_id": 577,
            "created": "Wed, 15 Jun 2022 12:58:29 UTC",
            "updated": "Wed, 15 Jun 2022 12:58:30 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "d9d58d6a-ecaa-11ec-9cb5-ac1f6bd4b988",
            "status": "CREATED",
            "hostname": "ltx1-app4225.stg.example.com",
            "inops_data": {
                "device_id": 1447220,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "J",
                "cabinet": "1717",
                "ru": 43,
                "environment": "STG",
                "warranty_start": 1579248000,
                "warranty_expiration": 1674028800,
                "location": "LTX1:J:1717:43",
                "created_time": 1580146354,
                "template_name": "DELL-DENSE-032-NVME-SSD",
                "template_group": "App node, 256G",
                "model": "DL C6420",
                "manufacturer": "Dell",
                "multiproducts": [
                    "venice-mon-du",
                    "ateneo-agent",
                    "venice-hooks-deployable",
                    "venice-backend"
                ],
                "services": [
                    "venice-mon-du",
                    "ateneo-agent",
                    "venice-hooks-deployable",
                    "venice-server"
                ]
            },
            "apps": [
                "venice-server",
                "venice-hooks-deployable",
                "venice-mon-du",
                "ateneo-agent",
                "venice-backend"
            ],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "smart_enabled"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "smart_enabled",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app4225.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "SMARTD has detected a drive that is failing.  This drive has passed thresholds for health checks.  When the drive fails or is replaced, the RAID array will have to perform data reconstruction, which is an expensive I/O process and can effect production applications. The SMARTD should have been enabled on this host but it is not.",
                    "is_manual": False,
                    "component": "SMART disabled on: {'sda'}",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 15 Jun 2022 12:58:29 UTC",
                    "updated": "Wed, 15 Jun 2022 12:58:29 UTC"
                }
            ]
        },
        {
            "cm_id": 576,
            "created": "Wed, 15 Jun 2022 10:37:55 UTC",
            "updated": "Wed, 15 Jun 2022 10:37:55 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "36de68ec-ec97-11ec-ad11-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "ltx1-app1542.stg.example.com",
            "inops_data": {
                "device_id": 266274,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "A",
                "cabinet": "602",
                "ru": 17,
                "environment": "PROD",
                "warranty_start": 0,
                "warranty_expiration": 1537254000,
                "location": "LTX1:A:602:17",
                "created_time": 1436197735,
                "template_name": "CSCO-UCSC220-010",
                "template_group": "Legacy",
                "model": "Cisco C220 M3",
                "manufacturer": "Cisco",
                "multiproducts": [
                    "flame-graph-data-pack",
                    "ats-tier-l0proxy",
                    "edge-collector"
                ],
                "services": [
                    "flame-graph-data-pack",
                    "edge-collector",
                    "l0proxy-ats"
                ]
            },
            "apps": [
                "edge-collector",
                "ats-tier-l0proxy",
                "flame-graph-data-pack",
                "l0proxy-ats"
            ],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "megaraid_full_health"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "megaraid_full_health",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.prod.example.com/ei-ltx1/api/v2/hosts/ltx1-app1542.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "One or More physical and virtual disks are not healthy. Hardware raid controller disk failure found. Operation can continue normally, but risk of data loss exists.",
                    "is_manual": False,
                    "component": "",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 15 Jun 2022 10:37:55 UTC",
                    "updated": "Wed, 15 Jun 2022 10:37:55 UTC"
                }
            ]
        },
        {
            "cm_id": 575,
            "created": "Wed, 15 Jun 2022 07:11:18 UTC",
            "updated": "Wed, 15 Jun 2022 07:11:18 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "59a545e8-ec7a-11ec-ad11-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "ltx1-app10023.stg.example.com",
            "inops_data": {
                "device_id": 1268387,
                "state": "Built",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "J",
                "cabinet": "1819",
                "ru": 51,
                "environment": "STG",
                "warranty_start": 1571382000,
                "warranty_expiration": 1666076400,
                "location": "LTX1:J:1819:51",
                "created_time": 1571687755,
                "template_name": "SM-STOR-032-SSD",
                "template_group": "Storage node",
                "model": "SM SKL storage 10G SFP+",
                "manufacturer": "SuperMicro",
                "multiproducts": [],
                "services": []
            },
            "apps": [],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "power"
            ],
            "check_ids": [
                "power_sm_psu_imbalance"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "power_sm_psu_imbalance",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app10023.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "power",
                    "team": "dctechs",
                    "description": "The power supplies on SuperMicro systems have imbalanced power outputs. This fails due to faulty power supplies that must be replaced.",
                    "is_manual": False,
                    "component": "Power imbalance: 128.9% (PSU1: 76W, PSU2: 174W)",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 15 Jun 2022 07:11:18 UTC",
                    "updated": "Wed, 15 Jun 2022 07:11:18 UTC"
                }
            ]
        },
        {
            "cm_id": 574,
            "created": "Wed, 15 Jun 2022 06:58:33 UTC",
            "updated": "Wed, 15 Jun 2022 06:58:33 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "91c37cd0-ec78-11ec-954b-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "lor1-0002842.int.example.com",
            "inops_data": {
                "device_id": 1052810,
                "state": "Production",
                "fabric": "ei4",
                "fabric_group": "ei",
                "site": "LOR1",
                "cage": "B",
                "cabinet": "423",
                "ru": 14,
                "environment": "STG",
                "warranty_start": 1552546800,
                "warranty_expiration": 1647158400,
                "location": "LOR1:B:423:14",
                "created_time": 1553698801,
                "template_name": "DELL-DENSE-031-NVME-SSD",
                "template_group": "App node, 128G",
                "model": "DL C6420",
                "manufacturer": "Dell",
                "multiproducts": [
                    "espresso-samzabeam-jobs",
                    "rosetta-gso-samza",
                    "groups-jobs",
                    "samza-frame-feature-generation-atc",
                    "ats-nearline",
                    "jobs-marketplace-samza",
                    "learning-enterprise-samza",
                    "waterloo-member-skill",
                    "cdp-samza-beam",
                    "learning-enterprise-reporting-samza",
                    "apply-integrations-samza",
                    "clt-samza-jobs",
                    "waterloo-std-job-company",
                    "waterloo-member-title",
                    "lss-workflow-samza",
                    "samza-yarn-espresso-demo",
                    "boris-test-samza1",
                    "content-notification-samzajob",
                    "group-platform-nearline"
                ],
                "services": [
                    "groups-existing-join-requests-auto-approval-fanout",
                    "boris-test-samza1-1",
                    "waterloo-member-skill-standardizer",
                    "groups-membership-invitation-dual-write-handler",
                    "lss-workflow-sales-entity-impression-processor",
                    "samza-identity-couchbase-upscale-bootstrap-integration",
                    "referred-candidate-update",
                    "cdms-enriched-unverified-companies-consumer",
                    "jobs-alternative-budget",
                    "espresso-identity-profile-bootstrap",
                    "clt-translation-response-processor",
                    "waterloo-member-title-standardizer",
                    "group-platform-nearline-processor",
                    "pages-views-milestone-eligibility-job",
                    "waterloo-std-job-company",
                    "cdp-crm-ingestion-status-updater",
                    "samza-nearline-feature-last-push-received-time",
                    "learning-enterprise-report-aggregate",
                    "ac-job-application-submission-status-tracker",
                    "learning-lms-integrations-video"
                ]
            },
            "apps": [
                "groups-existing-join-requests-auto-approval-fanout",
                "espresso-samzabeam-jobs",
                "boris-test-samza1-1",
                "waterloo-member-skill-standardizer",
                "rosetta-gso-samza",
                "groups-membership-invitation-dual-write-handler",
                "lss-workflow-sales-entity-impression-processor",
                "groups-jobs",
                "samza-identity-couchbase-upscale-bootstrap-integration",
                "samza-frame-feature-generation-atc",
                "referred-candidate-update",
                "cdms-enriched-unverified-companies-consumer",
                "ats-nearline",
                "jobs-marketplace-samza",
                "learning-enterprise-samza",
                "jobs-alternative-budget",
                "waterloo-member-skill",
                "espresso-identity-profile-bootstrap",
                "clt-translation-response-processor",
                "cdp-samza-beam",
                "learning-enterprise-reporting-samza",
                "waterloo-member-title-standardizer",
                "group-platform-nearline-processor",
                "apply-integrations-samza",
                "pages-views-milestone-eligibility-job",
                "clt-samza-jobs",
                "waterloo-std-job-company",
                "cdp-crm-ingestion-status-updater",
                "waterloo-member-title",
                "lss-workflow-samza",
                "samza-nearline-feature-last-push-received-time",
                "samza-yarn-espresso-demo",
                "boris-test-samza1",
                "learning-enterprise-report-aggregate",
                "ac-job-application-submission-status-tracker",
                "content-notification-samzajob",
                "group-platform-nearline",
                "learning-lms-integrations-video"
            ],
            "app_owners": [],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "power"
            ],
            "check_ids": [
                "power_dell_current_imbalance"
            ],
            "total_faults": 1,
            "blessin_enabled": False,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "power_dell_current_imbalance",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei4/api/v2/hosts/lor1-0002842.int.example.com?show_checks=true&show_extra=true",
                    "fault_type": "power",
                    "team": "dctechs",
                    "description": "The power supplies on Dell systems have imbalanced current outputs. This might be due to a system misconfiguration. To mitigate, run: 'racadm set System.ServerPwr.PSRedPolicy 0'",
                    "is_manual": False,
                    "component": "Current imbalance: 0.6A ({1: 1.6, 2: 1.0})",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Wed, 15 Jun 2022 06:58:33 UTC",
                    "updated": "Wed, 15 Jun 2022 06:58:33 UTC"
                }
            ]
        },
        {
            "cm_id": 571,
            "created": "Thu, 09 Jun 2022 01:52:14 UTC",
            "updated": "Tue, 14 Jun 2022 20:56:39 UTC",
            "created_by": "kreber",
            "last_updated_by": "kreber",
            "cm_uuid": "c85738b8-e796-11ec-bd64-ac1f6bd4b988",
            "status": "APPROVED",
            "hostname": "lor1-app18619.prod.example.com",
            "inops_data": {
                "device_id": 465334,
                "state": "Production",
                "fabric": "prod-lor1",
                "fabric_group": "prod",
                "site": "LOR1",
                "cage": "B",
                "cabinet": "302",
                "ru": 45,
                "environment": "PROD",
                "warranty_start": 1473836400,
                "warranty_expiration": 1568444400,
                "location": "LOR1:B:302:45",
                "created_time": 1475094641,
                "template_name": "SM-DENSE-020",
                "template_group": "App node, 64G",
                "model": "Fat Twin Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "nw-fuse-counting"
                ],
                "services": [
                    "fuse-server-counting"
                ]
            },
            "apps": [
                "fuse-server-counting"
            ],
            "app_owners": [
                "trustsre-blr@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "fan"
            ],
            "check_ids": [
                "cli_created_fan"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "kreber",
                    "check_id": "cli_created_fan",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "fan",
                    "team": "sysops",
                    "description": "test",
                    "is_manual": True,
                    "component": "fw-testing",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 09 Jun 2022 01:52:14 UTC",
                    "updated": "Thu, 09 Jun 2022 01:52:14 UTC"
                }
            ]
        },
        {
            "cm_id": 568,
            "created": "Thu, 26 May 2022 12:36:46 UTC",
            "updated": "Thu, 26 May 2022 12:36:46 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "80e5bd66-dcf0-11ec-9838-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "lva1-app4919.corp.example.com",
            "inops_data": {
                "device_id": 929317,
                "state": "Production",
                "fabric": "corp-lva1",
                "fabric_group": "corp",
                "site": "LVA1",
                "cage": "H",
                "cabinet": "508",
                "ru": 32,
                "environment": "CORP",
                "warranty_start": 1532415600,
                "warranty_expiration": 1627110000,
                "location": "LVA1:H:508:32",
                "created_time": 1533845793,
                "template_name": "SM-DENSE-030",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [],
                "services": []
            },
            "apps": [],
            "app_owners": [],
            "actionable": "no",
            "workflow_state": "Pending Approvals",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "manual test",
                    "is_manual": True,
                    "component": "test",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 12:36:46 UTC",
                    "updated": "Thu, 26 May 2022 12:36:46 UTC"
                }
            ]
        },
        {
            "cm_id": 566,
            "created": "Thu, 26 May 2022 12:36:39 UTC",
            "updated": "Tue, 31 May 2022 13:55:48 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "7d2f0fe2-dcf0-11ec-915f-ac1f6bd4b988",
            "status": "APPROVED",
            "hostname": "lva1-app5253.corp.example.com",
            "inops_data": {
                "device_id": 952353,
                "state": "Production",
                "fabric": "corp-lva1",
                "fabric_group": "corp",
                "site": "LVA1",
                "cage": "H",
                "cabinet": "508",
                "ru": 41,
                "environment": "CORP",
                "warranty_start": 1536217200,
                "warranty_expiration": 1630911600,
                "location": "LVA1:H:508:41",
                "created_time": 1536870447,
                "template_name": "SM-DENSE-030",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "pinot-server"
                ],
                "services": [
                    "pinot-server"
                ]
            },
            "apps": [
                "pinot-server"
            ],
            "app_owners": [
                "pinot-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "manual test",
                    "is_manual": True,
                    "component": "test",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 12:36:40 UTC",
                    "updated": "Thu, 26 May 2022 12:36:40 UTC"
                }
            ]
        },
        {
            "cm_id": 565,
            "created": "Thu, 26 May 2022 12:36:36 UTC",
            "updated": "Tue, 28 Jun 2022 07:01:58 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "7afdd33e-dcf0-11ec-9838-ac1f6bd50e76",
            "status": "APPROVED",
            "hostname": "lva1-app4495.corp.example.com",
            "inops_data": {
                "device_id": 826900,
                "state": "Production",
                "fabric": "corp-lva1",
                "fabric_group": "corp",
                "site": "LVA1",
                "cage": "H",
                "cabinet": "508",
                "ru": 36,
                "environment": "CORP",
                "warranty_start": 1529391600,
                "warranty_expiration": 1624086000,
                "location": "LVA1:H:508:36",
                "created_time": 1529611399,
                "template_name": "SM-DENSE-030",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [],
                "services": []
            },
            "apps": [
                "multiproduct-post-commit-mpdep"
            ],
            "app_owners": [
                "mp-pcx@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "manual test",
                    "is_manual": True,
                    "component": "test",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 12:36:36 UTC",
                    "updated": "Thu, 26 May 2022 12:36:36 UTC"
                }
            ]
        },
        {
            "cm_id": 563,
            "created": "Thu, 26 May 2022 12:31:20 UTC",
            "updated": "Tue, 31 May 2022 13:55:46 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "be7eba2a-dcef-11ec-8d3f-ac1f6bd50e76",
            "status": "APPROVED",
            "hostname": "lva1-app56724.prod.example.com",
            "inops_data": {
                "device_id": 1252924,
                "state": "Production",
                "fabric": "prod-lva1",
                "fabric_group": "prod",
                "site": "LVA1",
                "cage": "M",
                "cabinet": "815",
                "ru": 3,
                "environment": "PROD",
                "warranty_start": 1570086000,
                "warranty_expiration": 1664866800,
                "location": "LVA1:M:815:3",
                "created_time": 1570559208,
                "template_name": "DELL-DENSE-030-NVME-SSD",
                "template_group": "App node, 64G",
                "model": "DL C6420",
                "manufacturer": "Dell",
                "multiproducts": [
                    "rsvp"
                ],
                "services": [
                    "rsvp"
                ]
            },
            "apps": [
                "rsvp"
            ],
            "app_owners": [
                "growth-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "test manual",
                    "is_manual": True,
                    "component": "test",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 12:31:20 UTC",
                    "updated": "Thu, 26 May 2022 12:31:20 UTC"
                }
            ]
        },
        {
            "cm_id": 562,
            "created": "Thu, 26 May 2022 12:30:56 UTC",
            "updated": "Tue, 31 May 2022 14:48:33 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "b014f058-dcef-11ec-9838-ac1f6bd50e76",
            "status": "APPROVED",
            "hostname": "lva1-app59031.prod.example.com",
            "inops_data": {
                "device_id": 1385320,
                "state": "Production",
                "fabric": "prod-lva1",
                "fabric_group": "prod",
                "site": "LVA1",
                "cage": "M",
                "cabinet": "815",
                "ru": 15,
                "environment": "PROD",
                "warranty_start": 1575532800,
                "warranty_expiration": 1670227200,
                "location": "LVA1:M:815:15",
                "created_time": 1576002116,
                "template_name": "SM-DENSE-030-NVME-SSD",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "tscp-serving"
                ],
                "services": [
                    "tscp-index"
                ]
            },
            "apps": [
                "tscp-serving"
            ],
            "app_owners": [
                "adsrv-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "test manual",
                    "is_manual": True,
                    "component": "test",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 12:30:56 UTC",
                    "updated": "Thu, 26 May 2022 12:30:56 UTC"
                }
            ]
        },
        {
            "cm_id": 561,
            "created": "Thu, 26 May 2022 11:56:54 UTC",
            "updated": "Tue, 31 May 2022 13:55:46 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "ef422a98-dcea-11ec-a599-ac1f6bd4b988",
            "status": "APPROVED",
            "hostname": "ltx1-app0352.prod.example.com",
            "inops_data": {
                "device_id": 2087728,
                "state": "Production",
                "fabric": "prod-ltx1",
                "fabric_group": "prod",
                "site": "LTX1",
                "cage": "C",
                "cabinet": "312",
                "ru": 19,
                "environment": "PROD",
                "warranty_start": 1632207600,
                "warranty_expiration": 1726815600,
                "location": "LTX1:C:312:19",
                "created_time": 1633466857,
                "template_name": "DELL-DENSE-040-NVME-SSD",
                "template_group": "App node, 64G",
                "model": "DL C6420",
                "manufacturer": "Dell",
                "multiproducts": [
                    "vector-asset-manager",
                    "organization",
                    "ugc"
                ],
                "services": [
                    "vector-asset-manager",
                    "organization",
                    "ugc"
                ]
            },
            "apps": [
                "organization",
                "eis-backend",
                "vector-asset-manager"
            ],
            "app_owners": [
                "pages-sre@linkedin.com",
                "epc-sre@linkedin.com",
                "media-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk"
            ],
            "check_ids": [
                "cli_created_disk"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "This is test",
                    "is_manual": True,
                    "component": "test",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 11:56:54 UTC",
                    "updated": "Thu, 26 May 2022 11:56:54 UTC"
                }
            ]
        },
        {
            "cm_id": 559,
            "created": "Thu, 26 May 2022 11:52:57 UTC",
            "updated": "Tue, 31 May 2022 13:55:44 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "620abda2-dcea-11ec-9838-ac1f6bd50e76",
            "status": "APPROVED",
            "hostname": "ltx1-app3767.stg.example.com",
            "inops_data": {
                "device_id": 1090416,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "H",
                "cabinet": "2209",
                "ru": 32,
                "environment": "STG",
                "warranty_start": 1561618800,
                "warranty_expiration": 1656313200,
                "location": "LTX1:H:2209:32",
                "created_time": 1562866259,
                "template_name": "SM-DENSE-030-NVME-SSD",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "deadpool-ui-fe",
                    "deadpool-api"
                ],
                "services": [
                    "deadpool-ui-fe",
                    "deadpool-api"
                ]
            },
            "apps": [
                "deadpool-ui-fe",
                "deadpool-api"
            ],
            "app_owners": [
                "deadpool-team@linkedin.com",
                "sdi-dev@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "nvme_reboot"
            ],
            "check_ids": [
                "cli_created_nvme_reboot"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_nvme_reboot",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "This is for testing manual fault",
                    "is_manual": True,
                    "component": "test manual fault",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 11:52:57 UTC",
                    "updated": "Thu, 26 May 2022 11:52:57 UTC"
                }
            ]
        },
        {
            "cm_id": 558,
            "created": "Thu, 26 May 2022 11:51:32 UTC",
            "updated": "Tue, 31 May 2022 13:55:43 UTC",
            "created_by": "dudixit",
            "last_updated_by": "dudixit",
            "cm_uuid": "2f676e72-dcea-11ec-98bb-ac1f6bd50e76",
            "status": "APPROVED",
            "hostname": "lor1-4590.int.example.com",
            "inops_data": {
                "device_id": 1090467,
                "state": "Production",
                "fabric": "ei4",
                "fabric_group": "ei",
                "site": "LOR1",
                "cage": "B",
                "cabinet": "722",
                "ru": 32,
                "environment": "STG",
                "warranty_start": 1561618800,
                "warranty_expiration": 1656313200,
                "location": "LOR1:B:722:32",
                "created_time": 1562866261,
                "template_name": "SM-DENSE-030-NVME-SSD",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "deadpool-ui-fe",
                    "deadpool-api"
                ],
                "services": [
                    "deadpool-ui-fe",
                    "deadpool-api"
                ]
            },
            "apps": [
                "deadpool-ui-fe",
                "deadpool-api"
            ],
            "app_owners": [
                "deadpool-team@linkedin.com",
                "sdi-dev@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Get Server Ready",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "disk",
                "nvme_reboot"
            ],
            "check_ids": [
                "cli_created_disk",
                "cli_created_nvme_reboot"
            ],
            "total_faults": 2,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_disk",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "disk",
                    "team": "dctechs",
                    "description": "This is for testing manual fault",
                    "is_manual": True,
                    "component": "test manual fault",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 11:51:32 UTC",
                    "updated": "Thu, 26 May 2022 11:51:32 UTC"
                },
                {
                    "created_by": "dudixit",
                    "check_id": "cli_created_nvme_reboot",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "This is for testing manual fault",
                    "is_manual": True,
                    "component": "test manual fault",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Thu, 26 May 2022 11:52:56 UTC",
                    "updated": "Thu, 26 May 2022 11:52:56 UTC"
                }
            ]
        },
        {
            "cm_id": 556,
            "created": "Mon, 16 May 2022 15:57:29 UTC",
            "updated": "Mon, 16 May 2022 15:57:29 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "e2f3fd82-d530-11ec-be2b-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "ltx1-app0845.stg.example.com",
            "inops_data": {
                "device_id": 347212,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "F",
                "cabinet": "1005",
                "ru": 8,
                "environment": "STG",
                "warranty_start": 1449820800,
                "warranty_expiration": 1544428800,
                "location": "LTX1:F:1005:8",
                "created_time": 1450386020,
                "template_name": "SM-WEB-020",
                "template_group": "Legacy",
                "model": "6018R-TDLR-BK0-LC019",
                "manufacturer": "SuperMicro",
                "multiproducts": [],
                "services": []
            },
            "apps": [],
            "app_owners": [],
            "actionable": "no",
            "workflow_state": "Pending Approvals",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "virident"
            ],
            "check_ids": [
                "virident_flash"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "virident_flash",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app0845.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "virident",
                    "team": "dctechs",
                    "description": "A Virident card has failed. These cards are used on critical systems, so this a critical alert. Virident card flash headroom percentage of read only - bad flash is less than 2%. Please check.",
                    "is_manual": False,
                    "component": "vgca flash_headroom: 0.0",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Mon, 16 May 2022 15:57:29 UTC",
                    "updated": "Mon, 16 May 2022 15:57:29 UTC"
                }
            ]
        },
        {
            "cm_id": 553,
            "created": "Mon, 16 May 2022 11:52:32 UTC",
            "updated": "Mon, 16 May 2022 11:52:32 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "aa964782-d50e-11ec-be2b-ac1f6bd50e76",
            "status": "CREATED",
            "hostname": "ltx1-app0729.stg.example.com",
            "inops_data": {
                "device_id": 347983,
                "state": "Maintenance",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "F",
                "cabinet": "1002",
                "ru": 4,
                "environment": "STG",
                "warranty_start": 1449820800,
                "warranty_expiration": 1544428800,
                "location": "LTX1:F:1002:4",
                "created_time": 1450386041,
                "template_name": "SM-WEB-020",
                "template_group": "Legacy",
                "model": "6018R-TDLR-BK0-LC019",
                "manufacturer": "SuperMicro",
                "multiproducts": [],
                "services": []
            },
            "apps": [],
            "app_owners": [],
            "actionable": "no",
            "workflow_state": "Pending Approvals",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "virident"
            ],
            "check_ids": [
                "virident_lockfile"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "virident_lockfile",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app0729.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "virident",
                    "team": "sysops",
                    "description": "The Virident lockfile, /var/lib/vgc/loading.lock is present. With this lockfile present, the Virident driver did not start up cleanly. There could be a Virident card installed in this system that is not being monitored.  A system admin should remove this file and attempt to start the Virident driver via /etc/init.d/vgcd start to verify if the driver comes online.  Please do not leave an unused card in the system, they are expensive.",
                    "is_manual": False,
                    "component": "",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Mon, 16 May 2022 11:52:32 UTC",
                    "updated": "Mon, 16 May 2022 11:52:32 UTC"
                }
            ]
        },
        {
            "cm_id": 546,
            "created": "Mon, 09 May 2022 10:03:43 UTC",
            "updated": "Mon, 16 May 2022 10:22:16 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "4e30de24-cf7f-11ec-8fd2-ac1f6bd50e76",
            "status": "FINISHED_PLAN_EXECUTION",
            "hostname": "lor1-0002792.int.example.com",
            "inops_data": {
                "device_id": 1017540,
                "state": "Production",
                "fabric": "ei4",
                "fabric_group": "ei",
                "site": "LOR1",
                "cage": "B",
                "cabinet": "1622",
                "ru": 28,
                "environment": "STG",
                "warranty_start": 1544169600,
                "warranty_expiration": 1638864000,
                "location": "LOR1:B:1622:28",
                "created_time": 1544743659,
                "template_name": "SM-DENSE-030",
                "template_group": "App node, 64G",
                "model": "Fat Twin Skylake or CXL Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "databus-monitor",
                    "databus2",
                    "databus-events"
                ],
                "services": [
                    "databus-monitor",
                    "databus2-relay",
                    "databus-schemas"
                ]
            },
            "apps": [
                "databus-monitor",
                "databus-schemas",
                "databus2-relay"
            ],
            "app_owners": [
                "databus-sre@linkedin.com",
                "streaming-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Resolve Fault",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "power",
                "nvme_reboot",
                "memory",
                "fusion"
            ],
            "check_ids": [
                "ssd_device",
                "cli_created_fusion",
                "cli_created_power",
                "cli_created_memory"
            ],
            "total_faults": 4,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "ssd_device",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei4/api/v2/hosts/lor1-0002792.int.example.com?show_checks=true&show_extra=true",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "A NVME SSD has disappeared from the system. Typically, rebooting the machine brings the device back by resetting the NVME bus and the SSD actually is fine. SYSOPS/DCTECHS should work with SRE on rebooting the machine, but likely, their app is hosed any ways. If this is in error and NVME SSDs were intentionally removed from the system, then please remove the device",
                    "is_manual": False,
                    "component": "Installed SSDs: []",
                    "jira_ticket": "DCTECHS-204532",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204532",
                    "created": "Mon, 09 May 2022 10:03:43 UTC",
                    "updated": "Thu, 12 May 2022 17:51:46 UTC"
                },
                {
                    "created_by": "kreber",
                    "check_id": "cli_created_fusion",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "fusion",
                    "team": "dctechs",
                    "description": "test",
                    "is_manual": True,
                    "component": "testing",
                    "jira_ticket": "DCTECHS-204532",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204532",
                    "created": "Mon, 09 May 2022 18:32:53 UTC",
                    "updated": "Thu, 12 May 2022 17:51:46 UTC"
                },
                {
                    "created_by": "cfajardo",
                    "check_id": "cli_created_power",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "power",
                    "team": "dctechs",
                    "description": "test fault",
                    "is_manual": True,
                    "component": "testing-deadpoolUI",
                    "jira_ticket": "DCTECHS-204532",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204532",
                    "created": "Tue, 10 May 2022 03:26:26 UTC",
                    "updated": "Thu, 12 May 2022 17:51:46 UTC"
                },
                {
                    "created_by": "rbhanot",
                    "check_id": "cli_created_memory",
                    "detection_system": "manual",
                    "health_check_url": "",
                    "fault_type": "memory",
                    "team": "dctechs",
                    "description": "Test",
                    "is_manual": True,
                    "component": "faulty dimm",
                    "jira_ticket": "",
                    "jira_url": "",
                    "created": "Mon, 16 May 2022 10:17:43 UTC",
                    "updated": "Mon, 16 May 2022 10:17:43 UTC"
                }
            ]
        },
        {
            "cm_id": 545,
            "created": "Mon, 09 May 2022 10:03:42 UTC",
            "updated": "Tue, 10 May 2022 00:08:51 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "4d8e1acc-cf7f-11ec-8fd2-ac1f6bd50e76",
            "status": "FINISHED_PLAN_EXECUTION",
            "hostname": "ltx1-app0626.stg.example.com",
            "inops_data": {
                "device_id": 348085,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "F",
                "cabinet": "918",
                "ru": 39,
                "environment": "STG",
                "warranty_start": 1449820800,
                "warranty_expiration": 1544428800,
                "location": "LTX1:F:918:39",
                "created_time": 1450386043,
                "template_name": "SM-WEB-020",
                "template_group": "Legacy",
                "model": "6018R-TDLR-BK0-LC019",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "lix-backend"
                ],
                "services": [
                    "lix-backend"
                ]
            },
            "apps": [
                "lix-backend"
            ],
            "app_owners": [
                "trex-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Resolve Fault",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "nvme_reboot"
            ],
            "check_ids": [
                "ssd_device"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "ssd_device",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app0626.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "A NVME SSD has disappeared from the system. Typically, rebooting the machine brings the device back by resetting the NVME bus and the SSD actually is fine. SYSOPS/DCTECHS should work with SRE on rebooting the machine, but likely, their app is hosed any ways. If this is in error and NVME SSDs were intentionally removed from the system, then please remove the device",
                    "is_manual": False,
                    "component": "Installed SSDs: []",
                    "jira_ticket": "DCTECHS-204529",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204529",
                    "created": "Mon, 09 May 2022 10:03:42 UTC",
                    "updated": "Tue, 10 May 2022 00:08:52 UTC"
                }
            ]
        },
        {
            "cm_id": 544,
            "created": "Mon, 09 May 2022 10:03:28 UTC",
            "updated": "Tue, 10 May 2022 00:34:38 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "45266c72-cf7f-11ec-914f-ac1f6bd50e76",
            "status": "FINISHED_PLAN_EXECUTION",
            "hostname": "ltx1-app1950.stg.example.com",
            "inops_data": {
                "device_id": 494705,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "F",
                "cabinet": "812",
                "ru": 36,
                "environment": "STG",
                "warranty_start": 1480665600,
                "warranty_expiration": 1575273600,
                "location": "LTX1:F:812:36",
                "created_time": 1481303434,
                "template_name": "SM-WEB-020-NVME-10GT",
                "template_group": "Legacy",
                "model": "Supermicro NVME 10G copper web node",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "cs-network",
                    "training-lps-b-0205",
                    "language-packs",
                    "training-lps-obarik-2511",
                    "jobs-billing",
                    "learning-login-frontend",
                    "ac-hub-web",
                    "in-logstash",
                    "sales-payable-service",
                    "mobile-static-content",
                    "voyager-api"
                ],
                "services": [
                    "training-lps-b-0205",
                    "training-lps-obarik-2511",
                    "language-packs",
                    "cs-ds",
                    "jobs-billing",
                    "learning-login-frontend",
                    "ac-hub-web",
                    "in-logstash",
                    "voyager-api-jobs",
                    "sales-payable-service",
                    "mobile-static-content"
                ]
            },
            "apps": [
                "language-packs",
                "cs-ds",
                "jobs-billing",
                "learning-login-frontend",
                "ac-hub-web",
                "in-logstash",
                "voyager-api-jobs",
                "sales-payable-service",
                "mobile-static-content"
            ],
            "app_owners": [
                "k2-sre@linkedin.com",
                "epc-sre@linkedin.com",
                "learning-sre@linkedin.com",
                "identity-sre@linkedin.com",
                "growth-sre@linkedin.com",
                "trustsre-blr@linkedin.com",
                "careers-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Resolve Fault",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "nvme_reboot"
            ],
            "check_ids": [
                "ssd_device"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "ssd_device",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app1950.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "A NVME SSD has disappeared from the system. Typically, rebooting the machine brings the device back by resetting the NVME bus and the SSD actually is fine. SYSOPS/DCTECHS should work with SRE on rebooting the machine, but likely, their app is hosed any ways. If this is in error and NVME SSDs were intentionally removed from the system, then please remove the device",
                    "is_manual": False,
                    "component": "Installed SSDs: []",
                    "jira_ticket": "DCTECHS-204530",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204530",
                    "created": "Mon, 09 May 2022 10:03:28 UTC",
                    "updated": "Tue, 10 May 2022 00:34:39 UTC"
                }
            ]
        },
        {
            "cm_id": 543,
            "created": "Mon, 09 May 2022 10:03:26 UTC",
            "updated": "Tue, 10 May 2022 00:54:56 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "44a2d3b2-cf7f-11ec-8acd-ac1f6bd4b988",
            "status": "FINISHED_PLAN_EXECUTION",
            "hostname": "ltx1-app1722.stg.example.com",
            "inops_data": {
                "device_id": 494395,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "F",
                "cabinet": "808",
                "ru": 52,
                "environment": "STG",
                "warranty_start": 1480665600,
                "warranty_expiration": 1575273600,
                "location": "LTX1:F:808:52",
                "created_time": 1481303053,
                "template_name": "SM-WEB-020-NVME-10GT",
                "template_group": "Legacy",
                "model": "Supermicro NVME 10G copper web node",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "messaging-data-integrity-mt"
                ],
                "services": [
                    "messaging-data-integrity-mt"
                ]
            },
            "apps": [
                "messaging-data-integrity-mt"
            ],
            "app_owners": [
                "messaging-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Resolve Fault",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "nvme_reboot"
            ],
            "check_ids": [
                "ssd_device"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "ssd_device",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app1722.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "A NVME SSD has disappeared from the system. Typically, rebooting the machine brings the device back by resetting the NVME bus and the SSD actually is fine. SYSOPS/DCTECHS should work with SRE on rebooting the machine, but likely, their app is hosed any ways. If this is in error and NVME SSDs were intentionally removed from the system, then please remove the device",
                    "is_manual": False,
                    "component": "Installed SSDs: []",
                    "jira_ticket": "DCTECHS-204531",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204531",
                    "created": "Mon, 09 May 2022 10:03:27 UTC",
                    "updated": "Tue, 10 May 2022 00:54:57 UTC"
                }
            ]
        },
        {
            "cm_id": 542,
            "created": "Mon, 09 May 2022 10:03:21 UTC",
            "updated": "Tue, 10 May 2022 00:07:45 UTC",
            "created_by": "Nurse",
            "last_updated_by": "Nurse",
            "cm_uuid": "410d8f8a-cf7f-11ec-914f-ac1f6bd50e76",
            "status": "FINISHED_PLAN_EXECUTION",
            "hostname": "ltx1-app2578.stg.example.com",
            "inops_data": {
                "device_id": 757839,
                "state": "Production",
                "fabric": "ei-ltx1",
                "fabric_group": "ei",
                "site": "LTX1",
                "cage": "H",
                "cabinet": "415",
                "ru": 14,
                "environment": "STG",
                "warranty_start": 1525762800,
                "warranty_expiration": 1620457200,
                "location": "LTX1:H:415:14",
                "created_time": 1526078668,
                "template_name": "SM-DENSE-021",
                "template_group": "App node, 256G",
                "model": "Fat Twin Server Module",
                "manufacturer": "SuperMicro",
                "multiproducts": [
                    "samza-admin",
                    "samza-yarn"
                ],
                "services": [
                    "samza-yarn-nodemanager",
                    "samza-rest-service"
                ]
            },
            "apps": [
                "samza-yarn-nodemanager",
                "samza-rest-service"
            ],
            "app_owners": [
                "samza-sre@linkedin.com"
            ],
            "actionable": "yes",
            "workflow_state": "Resolve Fault",
            "hooks_phase_name": "",
            "hooks_phase_status": "",
            "hooks_enabled": False,
            "hooks_plan_id": "",
            "fault_types": [
                "nvme_reboot"
            ],
            "check_ids": [
                "ssd_device"
            ],
            "total_faults": 1,
            "blessin_enabled": True,
            "faults": [
                {
                    "created_by": "Nurse",
                    "check_id": "ssd_device",
                    "detection_system": "obhc",
                    "health_check_url": "https://obhc-api.stg.example.com/ei-ltx1/api/v2/hosts/ltx1-app2578.stg.example.com?show_checks=true&show_extra=true",
                    "fault_type": "nvme_reboot",
                    "team": "dctechs",
                    "description": "A NVME SSD has disappeared from the system. Typically, rebooting the machine brings the device back by resetting the NVME bus and the SSD actually is fine. SYSOPS/DCTECHS should work with SRE on rebooting the machine, but likely, their app is hosed any ways. If this is in error and NVME SSDs were intentionally removed from the system, then please remove the device",
                    "is_manual": False,
                    "component": "Installed SSDs: []",
                    "jira_ticket": "DCTECHS-204528",
                    "jira_url": "https://jira-stg.corp.example.com:8443/browse/DCTECHS-204528",
                    "created": "Mon, 09 May 2022 10:03:21 UTC",
                    "updated": "Tue, 10 May 2022 00:07:47 UTC"
                }
            ]
        }
    ]
}