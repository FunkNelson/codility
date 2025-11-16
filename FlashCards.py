import random

cardStack = {
    'Golden Signals': 'Latency\nTraffic\nError Rates\nSaturation',
    '3 Pillars of Observability': 'Logs\nMetrics\nTraces',
    'Latency': 'Time it takes for a request to travel from the client to the server and back\nOne of the observability golden signals',
    'Traffic': 'Number of requests a system receives over a specific period\nMeasured in requests per second (RPS), transactions per second (TPS), or bits per second (bps)\nOne of the observability golden signals',
    'Errors (Monitoring)': 'Percentage of requests resulting in errors, such as 404 Page Not Found or 500 Internal Server errors\nOne of the observability golden signals',
    'Saturation': 'Measures resource utilization, including CPU, memory and disk space\nOne of the observability golden signals',
    'VPC': 'Virtual Private Cloud\nIsolated virtual network in AWS\nYou define IP address range, subnets, route tables, and gateways',
    'VPN': 'Virtual Private Network\nSecure connection over public network\nEncrypts data in transit\nCommonly used to connect on-premises networks to cloud resources',
    'Traceroute': 'Network diagnostic tool\nDisplays path packets take from source to destination\nShows each hop along the route and time taken for each hop\nHelps identify network issues and latency',
    'Subnet': 'CIDR block portion of a VPC\nLives in Availability Zones\nPublic: Has route to Internet Gateway\nPrivate: Does not have route to Internet Gateway',
    'IGW': 'Internet Gateway\nAllows communication between VPC and internet\nAttached to VPC\nRoute table must have route to IGW for public subnet',
    'SG': 'Security Group\nStateful\nOperates at instance level\nSupports allow rules only\nEvaluated after NACLs',
    'EC2': 'Elastic Compute Cloud\nVirtual servers in the cloud\nProvides resizable compute capacity\nSupports various instance types optimized for different use cases',
    'EBS': 'Elastic Block Store\nBlock-level storage volumes for use with EC2 instances\nProvides persistent storage that can be attached to and detached from instances\nSupports various volume types optimized for different performance and cost requirements',
    'RDS': 'Relational Database Service\nManaged relational database service\nSupports multiple database engines (MySQL, PostgreSQL, Oracle, SQL Server, etc.)\nHandles database administration tasks such as backups, patching, and scaling',
    'KMS': 'Key Management Service\nManaged service for creating and controlling encryption keys\nEnables secure encryption of data at rest and in transit\nIntegrates with other AWS services for seamless encryption management',
    'Secrets Manager': 'Service for securely storing and managing sensitive information such as database credentials, API keys, and other secrets\nProvides automatic rotation, secure access, and auditing capabilities\nIntegrates with AWS services and applications for seamless secret management',
    'Well-Architected Framework': 'Operational Excellence\nSecurity\nReliability\nPerformance Efficiency\nCost Optimization',
    'Fault Tolerance': 'Ability of a system to continue operating properly in the event of the failure of some of its components\nAchieved through redundancy, failover mechanisms, and distributed architectures\nMinimizes downtime and ensures high availability',
    'High Availability': 'Designing systems to be operational and accessible for a high percentage of time\nAchieved through redundancy, failover mechanisms, and distributed architectures\nMinimizes downtime and ensures continuous access to services',
    'Blue/Green Deployment': 'Deployment strategy that reduces downtime and risk by running two identical production environments (Blue and Green)\nTraffic is routed to the Blue environment while the Green environment is updated\nOnce the Green environment is verified, traffic is switched to it, making it the new production environment',
    'Canary Deployment': 'Deployment strategy that gradually rolls out changes to a small subset of users before deploying to the entire user base\nAllows for monitoring and validation of changes in a controlled manner\nHelps identify issues early and minimizes the impact of potential failures',
    'Auto Scaling Group': 'Collection of EC2 instances treated as a logical grouping for automatic scaling and management\nEnsures the desired number of instances are running based on defined policies\nSupports scaling in and out based on demand',
    'CI/CD': 'Continuous Integration/Continuous Deployment\nPractices for automating the build, testing, and deployment of applications\nEnables faster and more reliable software delivery\nCommon tools: AWS CodePipeline, Jenkins, GitLab CI/CD',
    'IaC': 'Infrastructure as Code\nPractice of managing and provisioning infrastructure using code and automation tools\nEnables version control, repeatable deployments, and easier management of complex infrastructures\nCommon tools: AWS CloudFormation, Terraform, Ansible',
    'GitOps': 'Operational model that uses Git as the single source of truth for infrastructure and application code\nEnables collaboration, version control, and automated deployments\nIntegrates with CI/CD pipelines for continuous delivery',
    'RESTful API': 'Stateless\nClient-server architecture\nCacheable responses\nUniform interface\nLayered system\nCode on demand (optional)',
    'Disaster Recovery': 'Strategies to recover from catastrophic failures\nBackup and Restore\nPilot Light\nWarm Standby\nMulti-Site',
    'Lifecycle Hook': 'Feature of Auto Scaling Groups that allows you to perform custom actions when instances launch or terminate\nEnables you to pause the instance lifecycle to perform tasks such as configuration, software installation, or data backup before the instance becomes available or is terminated',
    'Lifecycle Policy': 'Defines the actions to be taken during the lifecycle of an Auto Scaling Group instance\nSpecifies the conditions under which instances are launched or terminated\nCan include scaling policies, health checks, and instance refresh settings',
    'Route Table': 'Set of rules (routes) that determine where network traffic is directed\nAssociated with subnets in a VPC\nContains routes to local VPC, IGW, NAT Gateway, peered VPCs, etc.',
    'NAT Gateway': 'Network Address Translation Gateway\nEnables instances in a private subnet to connect to the internet or other AWS services\nPrevents inbound traffic from the internet to those instances\nRequires an Elastic IP address',
    'S3 Endpoint': 'Enables private connections between a VPC and S3 without using an internet gateway, NAT device, VPN connection, or AWS Direct Connect\nTraffic between the VPC and S3 does not leave the Amazon network\nImproves security and reduces data transfer costs',
    'NACL': 'Network Access Control List\nStateless\nOperates at subnet level\nSupports allow and deny rules\nEvaluated before security groups',
    'ALB': 'Application Load Balancer\nDistributes incoming network traffic across multiple targets (webservers or containers) based on the content of the application-level requests\nOperates at 7th layer of OSI model\nCan inspect HTTP(S) request data',
    'AMI': 'Amazon Machine Image\nPreconfigured template required to launch EC2\nIncludes OS, software packages, custom files\nUsed by autoscaling and disaster recovery',
    'Route 53': 'DNS lookup\nProvide IP address associated with domain name\nCan point to CloudFront, S3, Load Balancer, EC2, Static IP\nCan be used to register domains',
    'AWS Physical and Networking Layers': 'Regions, Availability Zones, Edge Locations',
    'Region': 'General geographic area for AWS physical and networking resources\nExamples: us-east-1, eu-central-1',
    'Availability Zone': 'Isolated datacenters within regions\nExamples: us-east-1a, 1b, 1c, 1d',
    'Edge Location': 'Smaller datacenters in most cities\nUsed by Route53 and CloudFront to cache content close to endusers for better performance',
    'Horizontal Scaling': 'Increase compute capacity by increasing number of instances',
    'Vertical Scaling': 'Increase compute capacity by migrating to larger instances',
    'CloudFront': 'Content Delivery Network (CDN)\nCaches copies of static content at Edge Locations globally\nReduces latency by serving content from nearest edge location to user',
    'CloudFormation': 'Infrastructure as Code (IaC)\nAutomates provisioning and management of AWS resources using templates\nEnables version control, repeatable deployments, and easier management of complex infrastructures',
    'NACL': 'Network Access Control List\nStateless\nOperates at subnet level\nSupports allow and deny rules\nEvaluated before security groups',
    'EMR': 'Elastic Map Reduce\nManaged Hadoop framework\nProcesses large datasets across resizable clusters of EC2 instances\nUsed for big data analytics, machine learning, and data processing tasks',
    'SSH Key Pair': 'Authentication method for securely accessing EC2 instances\nConsists of a public key (stored on the instance) and a private key (held by the user)\nUsed to establish encrypted SSH connections to Linux instances',
    'Lambda': 'Serverless compute service\nRuns code in response to events without provisioning or managing servers\nAutomatically scales based on demand\nSupports multiple programming languages',
    'SQS': 'Simple Queue Service\nFully managed message queuing service\nEnables decoupling and scaling of microservices, distributed systems, and serverless applications\nSupports standard and FIFO queues',
    'SNS': 'Simple Notification Service\nFully managed publish/subscribe messaging service\nEnables decoupling of microservices, distributed systems, and serverless applications\nSupports multiple protocols including HTTP/S, email, SMS, and Lambda functions',
    'Message Queue': 'Communication method between distributed components\nStores messages until they are processed and deleted by the consumer\nEnables asynchronous communication and decoupling of components',
    'FIFO': 'First In, First Out\nMessage processing order where the first message sent to the queue is the first one to be received and processed\nEnsures strict ordering of messages\nCommonly used in scenarios where the order of operations is critical',
    'FILO': 'First In, Last Out\nMessage processing order where the first message sent to the queue is the last one to be received and processed\nLess common than FIFO\nUsed in specific scenarios where reverse order processing is required',
    'Short Polling': 'Method of retrieving messages from an SQS queue where the consumer makes a request to the queue and immediately receives any available messages\nIf no messages are available, the request returns an empty response\nCan result in higher latency and increased costs due to frequent polling',
    'Long Polling': 'Method of retrieving messages from an SQS queue where the consumer makes a request to the queue and waits for a specified duration (up to 20 seconds) for messages to become available\nReduces latency and costs by minimizing the number of empty responses\nImproves efficiency of message retrieval',
    'STS': 'Security Token Service\nWeb service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users)\nUseful for granting access to AWS resources without sharing long-term credentials',
    'Federation': 'Process of allowing users from an external identity provider (IdP) to access AWS resources without creating separate IAM users\nUses standards like SAML, OIDC, or OAuth\nEnables single sign-on (SSO) and centralized user management',
    'Headless User': 'IAM user without console access\nUsed for programmatic access to AWS resources via APIs, CLI, or SDKs\nTypically associated with applications, services, or automation scripts',
    'Evenutal Consistency': 'Data replication model where updates to a data store may not be immediately visible to all read operations\nOver time, all replicas will converge to the same state\nCommon in distributed systems to improve performance and availability (ex: S3)',
    'VPC Peering': 'Networking connection between two VPCs that enables routing of traffic between them using private IP addresses\nCan be established within the same AWS account or across different AWS accounts\nDoes not require a gateway, VPN connection, or separate network appliance',
    'ECS': 'Elastic Container Service\nFully managed container orchestration service\nSupports Docker containers\nEnables easy deployment, management, and scaling of containerized applications\nIntegrates with other AWS services like IAM, VPC, and CloudWatch',
    'EKS': 'Elastic Kubernetes Service\nFully managed Kubernetes service\nSimplifies deployment, management, and scaling of containerized applications using Kubernetes\nHandles tasks like cluster provisioning, patching, and scaling\nIntegrates with other AWS services for security, networking, and monitoring',
    'CloudWatch': 'Monitoring and observability service\nCollects and tracks metrics, logs, and events from AWS resources and applications\nProvides dashboards, alarms, and automated actions based on defined thresholds\nHelps gain insights into system performance and operational health',
    'DogStatsD': 'A statsd-compatible daemon for aggregating statistics, such as counters and timers, sent over UDP or TCP and sending aggregates to one or more pluggable backend services\nOften used for application performance monitoring and metrics collection',
    'StatsD': 'A network daemon that listens for statistics, like counters and timers, sent over UDP or TCP and sends aggregates to one or more pluggable backend services\nCommonly used for application performance monitoring and metrics collection',
    'OpenTelemetry': 'An open-source observability framework for cloud-native software\nProvides APIs, libraries, agents, and instrumentation to collect metrics, logs, and traces from applications and infrastructure\nSupports multiple programming languages and integrates with various backend systems for analysis and visualization',
    'Prometheus': 'An open-source systems monitoring and alerting toolkit\nCollects and stores metrics as time series data\nProvides a powerful query language (PromQL) for querying and analyzing metrics\nOften used in conjunction with Grafana for visualization',
    'Grafana': 'An open-source platform for monitoring and observability\nProvides tools for visualizing time series data from various data sources, including Prometheus, InfluxDB, and Elasticsearch\nEnables the creation of customizable dashboards and alerts for monitoring system performance and health',
    'ELK Stack': 'Elasticsearch, Logstash, and Kibana\nA popular open-source stack for log management and analysis\nElasticsearch: Search and analytics engine\nLogstash: Data processing pipeline for collecting, parsing, and storing logs\nKibana: Visualization tool for exploring and analyzing log data',
    'Kibana': 'A data visualization and exploration tool\nPart of the ELK Stack (Elasticsearch, Logstash, Kibana)\nProvides a web interface for creating dashboards and visualizations based on data stored in Elasticsearch\nUsed for log analysis, monitoring, and reporting',
    'Datadog HTTP API': 'A RESTful API provided by Datadog that allows users to programmatically send metrics, events, and service checks to their Datadog account\nEnables integration with custom applications and services for monitoring and observability purposes',
    'Elasticsearch': 'A distributed, RESTful search and analytics engine\nPart of the ELK Stack (Elasticsearch, Logstash, Kibana)\nStores and indexes large volumes of data for fast search and analysis\nCommonly used for log and event data analysis, full-text search, and real-time analytics',
    'Logstash': 'A server-side data processing pipeline\nPart of the ELK Stack (Elasticsearch, Logstash, Kibana)\nCollects, parses, and transforms log and event data from various sources\nSends processed data to Elasticsearch for storage and analysis',
    'Datadog Agent': 'A lightweight software that runs on your hosts to collect metrics, traces, and logs from your applications and infrastructure\nSends the collected data to the Datadog platform for monitoring, analysis, and visualization\nSupports a wide range of integrations with popular technologies and services',
    'IAM Role': 'An IAM entity that defines a set of permissions for making AWS service requests\nCan be assumed by trusted entities such as AWS services, applications, or users\nUsed to grant temporary access to AWS resources without sharing long-term credentials',
    'IAM Policy': 'A JSON document that defines permissions for an IAM user, group, or role\nSpecifies allowed or denied actions on AWS resources\nCan be managed (predefined by AWS) or customer-managed (created by users)\nUsed to control access to AWS services and resources',
    'CloudTrail': 'AWS service that enables governance, compliance, operational auditing, and risk auditing of your AWS account\nRecords AWS API calls and events for your account and delivers log files to an S3 bucket\nHelps track changes to AWS resources and monitor user activity',
    'VPC Flow Logs': 'Feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC\nFlow log data can be published to Amazon CloudWatch Logs or Amazon S3\nUseful for monitoring network traffic, troubleshooting connectivity issues, and enhancing security analysis',
    'Observability': 'Ability to measure the internal states of a system by examining its outputs\nAchieved through collecting and analyzing logs, metrics, and traces\nHelps understand system behavior, diagnose issues, and improve performance',
    'O11y': 'Abbreviation for Observability\nRefers to the practice of measuring and understanding the internal states of a system through its outputs\nInvolves collecting and analyzing logs, metrics, and traces to gain insights into system behavior and performance',
    'Observability vs. Monitoring': 'Monitoring: Focuses on collecting predefined metrics and logs to track system health and performance\nObservability: Encompasses monitoring but also includes the ability to explore and analyze data to understand system behavior and diagnose issues\nObservability provides deeper insights into complex systems compared to traditional monitoring',
    'SaaS architecture': 'Software as a Service\nCloud computing model where applications are hosted by a service provider and made available to users over the internet\nEliminates the need for users to install and maintain software on their local devices\nExamples: Google Workspace, Salesforce, Dropbox'
}


keys_list = list(cardStack.keys())
width = 50
session_active = True


def displayCard(card):
    print('\n')
    print(f" ------------------------------------------------ ")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(card.center(width))
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f" ------------------------------------------------ ")


def printAnswer(card):
    print('\n')
    print(cardStack[card])
    print('\n')


while session_active:
    random_card = random.choice(keys_list)
    displayCard(random_card)
    input('Press Enter to flip the card')
    printAnswer(random_card)
    nextCard = input('Another card? (Y/N)')
    if nextCard.lower() == 'n':
        session_active = False
