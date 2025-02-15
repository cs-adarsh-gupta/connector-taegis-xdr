"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

get_assets_dict = {"Hostname": "hostname", "IP Address": "ip_address",
                   "MAC Address": "mac_address", "Tag": "tag", "Username": "username", "OS Version": "os_version",
                   "Endpoint Type": "endpoint_type", "Created At": "created_at", "Updated At": "updated_at",
                   "Deleted At": "deleted_at", "OS Family": "os_family", "OS Distributor": "os_distributor",
                   "Sensor Version": "sensor_version", "Ascending": "asc", "Descending": "desc"}

get_investigations_dict = {"Ascending": "asc", "Descending": "desc", "ID": "id", "Tenant ID": "tenant_id",
                           "Tags": "tags",
                           "Genesis Alerts": "genesis_alerts",
                           "Genesis Events": "genesis_events", "Alerts": "alerts", "Events": "events",
                           "Assets": "assets",
                           "Auth Credentials": "auth_credentials", "Key Findings": "key_findings",
                           "Description": "description",
                           "Notified At": "notified_at",
                           "Created By": "created_by", "Status": "status", "Contributors": "contributors",
                           "Service Desk ID": "service_desk_id", "Service Desk Type": "service_desk_type",
                           "All Alerts": "all_alerts", "All Events": "all_events", "Priority": "priority",
                           "Type": "type"}

update_alert_status_dict = {"Open": "OPEN", "True Positive Benign": "TRUE_POSITIVE_BENIGN",
                            "True Positive Malicious": "TRUE_POSITIVE_MALICIOUS", "False Positive": "FALSE_POSITIVE",
                            "Not Actionable": "NOT_ACTIONABLE", "Other": "OTHER", "Suppressed": "SUPPRESSED"}

server_url_dict = {"US-1": "https://api.ctpx.secureworks.com", "US-2": "https://api.delta.taegis.secureworks.com",
                   "US WEST": "https://api.foxtrot.taegis.secureworks.com",
                   "EU": "https://api.echo.taegis.secureworks.com"}

get_alerts_query = """
    query alertsServiceSearch($in: SearchRequestInput)
    {
        alertsServiceSearch(in: $in)
        {
            reason search_id status alerts { previous_offset total_results first_offset group_by { key value } last_offset next_offset total_parts list { resolution_reason third_party_details { generic { generic { record { key value } } name } } id parent_tenant_id metadata { confidence began_at { seconds nanos } full_title title severity_updated_at { seconds nanos } first_seen_at { seconds nanos } created_at { seconds nanos } inserted_at { seconds nanos } first_investigated_at { seconds nanos } description updated_at { seconds nanos } engine { version name } origin first_resolved_at { seconds nanos } creator { rule { version rule_id } detector { detector_id detector_name version } } ended_at { seconds nanos } severity } severity_history { id changed_at { seconds nanos } severity } enrichment_details { travel_features { prior_location { radius country_code_iso asn geohash ip_address longitude latitude } current_location { radius country_code_iso asn geohash ip_address longitude latitude } accurate_geo travel_speed_impossible long_distance_travel travel_km_min travel_hours foreign_travel travel_km_h_min username } account_compromise_detector_detail { user_name } whois { registrarName registrant_country administrativeContact_street1 registrant_street1 standardRegUpdatedDate registrant_faxExt administrativeContact_postalCode registrant_street2 administrativeContact_state administrativeContact_telephoneExt administrativeContact_street3 reg_created_date_usec registrant_state registrant_city administrativeContact_faxExt whoisServer contactEmail nameServers standardRegExpiresDate createdDate administrativeContact_email standardRegCreatedDate Audit_auditUpdatedDate registrant_postalCode reg_updated_date_usec expiresDate administrativeContact_telephone updatedDate administrativeContact_name registrant_telephoneExt administrativeContact_organization registrant_name domainName registrant_telephone administrativeContact_country registrant_organization registrant_street3 reg_expires_date_usec administrativeContact_street2 registrant_fax registrant_email status administrativeContact_fax registrant_street4 administrativeContact_street4 administrativeContact_city } mitre_attack_info { technique_id version technique url system_requirements contributors data_sources description defence_bypassed tactics type platform } trust_features { current_event_time_sec location { radius country_code_iso asn geohash ip_address longitude latitude } user_unknown_asn prior_event_time_sec network_unknown_asn user_unknown_ip current_event_id network_unknown_ip prior_event_id username } improbable_logon_detail { user_logon_baselines { feature_value days_in_baseline feature_frequency_in_org approximate_count_in_user feature_frequency_in_user } logon_anomaly { min_allowed_org_percentage feature_value feature_frequency_in_org min_allowed_user_percentage approximate_count_in_user feature_frequency_in_user } user feature_name source_address } auth_scan_detail { failed_logon_attempts { has_logon_success target_user_name num_attempts } total_attempts successful_logon_attempts { has_logon_success target_user_name num_attempts } } kerberoasting { suspicious_num_requests user_baseline total_spns user_avg_requests percentage_accessed hostname spns_accessed user_max_requests user source_address } geo_ip { radius country_code_iso asn geohash ip_address longitude latitude } watchlist_matches { details { reason attacks list_name } entity } login_failure { host target_address failed_auth_event user successful_auth_event source_address } rare_program_rare_ip { host connections { source_ip destination_ip } programs } password_spray_detail { num_auth_failures num_auth_successes all_affected_users { target_user_name target_domain_name user_had_auth_success } source_address } hands_on_keyboard_details { host_id num_admin_events total_num_events matched_num_events common_parent_image_path matched_process { process_resource_id score event_time_sec image { image_path matched_features } num_matched_features commandline { matched_features commandline } severity } username } generic { generic { record { key value } } name } dns_exfil { num_queries } tactic_graph_detail { graph_id events { key values } } brute_force_detail { most_recent_auths_failures { resource_record_identifier action win_event_id domain event_timestamp target_username } num_auth_successes last_successful_auth { resource_record_identifier action win_event_id domain event_timestamp target_username } num_auth_failures } ddos_source_ip { host_id sensor_id top_destination_ips { count ip_address } analytic_observable_min_count event_observable_count historical_ip_counts { date { seconds nanos } count } event_observable_count_std_dev baseline_observable_count_std_dev baseline_observable_count_mean analytic_time_threshold analytic_observable_std_dev_threshold hour_partition baseline_num_days baseline_observable_count_median } business_email_compromise { source_address_geo_summary { city { confidence name locale_names { record { key value } } geoname_id } location { radius metro_code timezone longitude us_metro_code gmt_offset latitude } asn { autonomous_system_org autonomous_system_no } country { confidence code iso_code geoname_id } continent { code geoname_id } } user_name source_address } } priority { version model_version model_name applied_time { seconds nanos } value prioritizer evidence } sensor_types events_metadata { began_at { seconds nanos } first_event_id last_event_id updated_at { seconds nanos } total_events ended_at { seconds nanos } } reference_details { reference { description url type } } group_key entities { relationships { to_entity relationship from_entity type } entities } event_ids { id } tags suppressed resolution_history { user_id timestamp { seconds nanos } id num_alerts_affected reason status } tenant_id key_entities { entity label } observation_ids { id } visibility suppression_rules { id version } alerting_rules { id version } collection_ids { id } status attack_technique_ids investigation_ids { id GenesisAlertsFlag } } part }
        }
    }
    """

get_assets_query = """
    query allAssets($offset: Int, $limit: Int, $order_by: AssetsOrderByInput, $order_direction: AssetsOrderDirectionInput, $filter_asset_state: AssetStateFilter, $only_most_recent: Boolean)
    {
        allAssets(offset: $offset, limit: $limit, order_by: $order_by, order_direction: $order_direction, filter_asset_state: $filter_asset_state, only_most_recent: $only_most_recent)
        {
            totalResults offset limit assets { id hostId rn tenantId sensorTenant sensorId ingestTime createdAt updatedAt deletedAt lastSeenAt biosSerial firstDiskSerial systemVolumeSerial sensorVersion endpointType endpointPlatform hostnames { id createdAt updatedAt hostId hostname } ethernetAddresses { id createdAt updatedAt hostId mac } ipAddresses { id createdAt updatedAt ip hostId } users { id createdAt updatedAt hostId username } architecture osFamily osVersion osDistributor osRelease systemType osCodename kernelRelease kernelVersion tags { id hostId tenantId createdAt updatedAt tag key } connectionStatus model cloudProviderName cloudInstanceId endpointGroup { id } status }
        }
    }
    """

get_endpoint_query = """query assetEndpointInfo($id: ID!)
{
    assetEndpointInfo(id: $id)
    {
       hostId hostName actualIsolationStatus allowedDomain desiredIsolationStatus firstConnectTime moduleHealth { enabled lastRunningTime moduleDisplayName } lastConnectAddress lastConnectTime sensorVersion    
    }
}
"""

get_investigations_query = """query investigationsSearch($page: Int, $perPage: Int, $query: String, $filterText: String, $orderByField: OrderFieldInput, $orderDirection: OrderDirectionInput)
    {
        investigationsSearch(page: $page, perPage: $perPage, query: $query, filterText: $filterText, orderByField: $orderByField, orderDirection: $orderDirection)
        {
            totalCount investigations { id investigationType tenant_id search_queries { id } first_notified_at notified_at transition_state { handed_off acknowledge_time resolved_at_least_once handoff_time initial_handoff_time resolution_time initial_resolution_time acknowledged initial_acknowledge_time acknowledged_at_least_once resolved handed_off_at_least_once } tenant_id description contributors genesis_events { id } events_count alerts2 { id } assignee { id email family_name name tenants { id name } status email_normalized user_id given_name email_verified roles } service_desk_type updated_at investigationType assets_count genesis_events_count alerts_count assignee_id tags created_by_scwx created_at created_by_partner activity_logs { id target comment tenant_id investigation_id description user_id created_at type updated_at } auth_credentials type events { id } assignee_user { id } rn deleted_at alerts { id } processing_status { events alerts assets } first_notified_at_scwx archived_at service_desk_id status genesis_alerts_count files_count created_by_user { id } priority assets { id } contributed_users { id } id created_by genesis_alerts { id } access_vectors { id name investigation_id mitre_info { data_sources tactics technique description platform technique_id system_requirements defence_bypassed contributors url version type } created_at updated_at } comments_count { parent_id unread parent_type total } latest_activity genesis_alerts2 { id } shortId key_findings }
        }
    }
"""

get_investigations_alerts_query = """query investigationAlerts($page: Int, $perPage: Int, $investigation_id: ID!)
{
     investigationAlerts(investigation_id: $investigation_id,page: $page, perPage: $perPage)
        {
            alerts { id } totalCount
        }
}
"""

get_playbook_execution_query = """query playbookExecution($playbookExecutionId: ID!)
{
    playbookExecution(playbookExecutionId: $playbookExecutionId)
    {
        id createdAt createdBy updatedAt updatedBy state tenant inputs outputs runId
    }
}
"""

get_user_by_id_query = """query tdruser($id: ID!, $excludeDeactivatedRoleAssignments: Boolean, $includeMaskedRelatedUsers: Boolean)
    {
        tdruser(id: $id, excludeDeactivatedRoleAssignments: $excludeDeactivatedRoleAssignments, includeMaskedRelatedUsers: $includeMaskedRelatedUsers)
        {
            id id_uuid user_id user_id_v1 created_at updated_at created_by updated_by last_login invited_date registered_date deactivated_date status status_localized email email_normalized family_name given_name phone_number phone_extension secondary_phone_number secondary_phone_extension roles tenants { id } tenants_v2 { id role } accessible_tenants { id name name_normalized enabled allow_response_actions actions_approver expires_at environments { name enabled } labels { id tenant_id name value } services { id name description } is_partner parent } role_assignments { id tenant_id role_id deactivated role_name role_display_name expires_at created_at updated_at allowed_environments } environments eula { date version } timezone tenant_status tenant_status_localized entitlement_channel allowed_entitlement_channels masked community_role is_scwx is_partner preferred_language pre_verified
        }
    }
"""

isolate_assets_query = """mutation isolateAsset($id: ID!, $reason: String!)
    {
        isolateAsset(id: $id, reason: $reason)
        {
           id hostId rn tenantId sensorTenant sensorId ingestTime createdAt updatedAt deletedAt biosSerial firstDiskSerial systemVolumeSerial sensorVersion endpointType endpointPlatform hostnames {id hostId hostname createdAt updatedAt} ethernetAddresses {id hostId createdAt updatedAt mac} ipAddresses {id ip hostId createdAt updatedAt}
        }
    }
"""

update_alert_status_query = """
        mutation alertsServiceUpdateResolutionInfo($in: UpdateResolutionRequestInput)
        {
            alertsServiceUpdateResolutionInfo(in: $in)
            {
                reason resolution_status
            }
        }
"""

update_investigation_query = """mutation updateInvestigation($investigation_id: ID!, $investigation: UpdateInvestigationInput!)
    {
        updateInvestigation(investigation_id: $investigation_id, investigation: $investigation)
        {
            id tenant_id tags alerts { id } events { id } assets {id} auth_credentials key_findings description created_at updated_at created_by status contributors service_desk_id service_desk_type assignee_id assignee {id name roles status user_id email} priority type closeReason alerts_count events_count rn shortId    
        }
    }
"""

unarchive_investigation_query = """mutation unArchiveInvestigation($investigation_id: ID!)
    {
        unArchiveInvestigation(investigation_id: $investigation_id)
        {
            id tenant_id tags alerts { id } events { id } assets {id} auth_credentials key_findings description created_at updated_at created_by status contributors service_desk_id service_desk_type assignee_id assignee {id name roles status user_id email} priority type closeReason alerts_count events_count rn shortId    
        }
    }
"""

add_alerts_to_investigation_query = """mutation addAlertsToInvestigation($investigation_id: ID!, $alerts: [String!]!)
    {
        addAlertsToInvestigation(investigation_id: $investigation_id, alerts: $alerts)
        {
            id tenant_id tags alerts { id } events { id } assets {id} auth_credentials key_findings description created_at updated_at created_by status contributors service_desk_id service_desk_type assignee_id assignee {id name roles status user_id email} priority type closeReason alerts_count events_count rn shortId    
        }
    }
"""

add_events_to_investigation_query = """mutation addEventsToInvestigation($investigation_id: ID!, $events: [String!]!)
    {
        addEventsToInvestigation(investigation_id: $investigation_id, events: $events)
        {
            id tenant_id tags alerts { id } events { id } assets {id} auth_credentials key_findings description created_at updated_at created_by status contributors service_desk_id service_desk_type assignee_id assignee {id name roles status user_id email} priority type closeReason alerts_count events_count rn shortId    
        }
    }
"""

create_investigation_query = """mutation createInvestigation($investigation: InvestigationInput!)
    {
        createInvestigation(investigation: $investigation)
        {
            id tenant_id tags alerts { id } events { id } assets {id} auth_credentials key_findings description created_at updated_at created_by status contributors service_desk_id service_desk_type assignee_id assignee {id name roles status user_id email} priority type closeReason alerts_count events_count rn shortId    
        }
    }
"""

execute_playbook_query = """mutation executePlaybookInstance($playbookInstanceId: ID!, $parameters: JSONObject)
{
    executePlaybookInstance(playbookInstanceId: $playbookInstanceId, parameters:$parameters)
    {
        id createdAt createdBy updatedAt updatedBy state tenant inputs outputs runId
    }
}
"""

create_comment_query = """mutation addCommentToInvestigation($input: AddCommentToInvestigationInput!)
    {
        addCommentToInvestigation(input : $input)
        {
            id createdAt updatedAt authorId comment investigationId tenantId mentionsIds readByIds isInternal author { id }
        }
    }
"""