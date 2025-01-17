CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'farah@diba123';

CREATE DATABASE SCOPED CREDENTIAL WorkspaceIdentity
WITH IDENTITY = 'Managed Identity'

--DROP EXTERNAL TABLE ActivityLog;
--DROP EXTERNAL DATA SOURCE srcActivityLog;


--CREATE EXTERNAL DATA SOURCE srcActivityLog
--WITH 
--(
--    LOCATION='https://dlsdp203famirshahi/data',
--    CREDENTIAL=sasToken
--)

CREATE EXTERNAL DATA SOURCE srcActivityLog
WITH 
(
    LOCATION='https://dlsdp203famirshahi/data',
    CREDENTIAL=WorkspaceIdentity
)

CREATE EXTERNAL FILE FORMAT parquetFileFormat WITH
(
    FORMAT_TYPE=PARQUET,
    DATA_COMPRESSION='org.apache.hadoop.io.compress.SnappyCodec'
)

CREATE EXTERNAL TABLE ActivityLog
(
   [Correlationid] varchar(200),
   [Operationname] varchar(300),
   [Status] varchar(100),
   [Eventcategory] varchar(100),
   [Level] varchar(100),
   [Time] varchar(100),
   [Subscription] varchar(200),
   [Eventinitiatedby] varchar(1000),
   [Resourcetype] varchar(300),
   [Resourcegroup] varchar(1000),
   [Resource] varchar(2000))
WITH (
    LOCATION='/ActivityLog01.parquet',
    DATA_SOURCE=srcActivityLog,
    FILE_FORMAT=parquetFileFormat
)

SELECT * FROM ActivityLog;

