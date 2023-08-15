# DSG Security Baseline: Azure Blob Storage

## TL;DR Brief Summary

> **Purpose:** 
> Added this text: Guidance and Security requirements for standing up and using an Azure Blob Storage SKU in an application.
>
> **Who:** 
>  Intended for ```Project Management``` and ```Development Teams``` and ```Security Architects or Security Relationship Managers``` looking to either use an Azure Blob Storage in their application or audit/review an applications use of an Azure Blob Storage.
>
> **What:** 
> Provide clear and concise guidance on how to deploy and use an Azure Blob Storage in the appropriate secure way.
>
> **Why:** 
> Azure Blob Storage often is used as transitory storage for an application and as such often either long term or short term holds sensitive data.  Due to this use case, proper security controls must be in place, especially when sensitive data is moving into or out of the Storage.
>

## Summary

```Azure Blob Storage``` is a service that provides object storage for the cloud. Objects stored in a Blob Storage can be of any type.

## Azure Blob Storage Controls

### Control Title: Enable encryption for Azure Blob Storage from KEN

| Control ID | Description | Objective |
| -- | -- | -- |
| A1 | This control ensures that Azure Blob Storage data is encrypted at rest. | To protect Azure Blob Storage data from unauthorized access. |

#### Control Implementation Steps

| Steps | Reference |
| ----- | --------- |
| Enable encryption for Azure Blob Storage. | https://docs.microsoft.com/en-us/azure/storage/blobs/encryption-how-to |

#### Control Audit Steps
| Steps |
| ----- |
| [Verify that Azure Blob Storage is encrypted.](https://docs.microsoft.com/en-us/azure/storage/blobs/encryption-how-to#verify-encryption) |
### Control Title: Configure access control for Azure Blob Storage

| Control ID | Description | Objective |
| -- | -- | -- |
| A2 | This control ensures that only authorized users can access Azure Blob Storage data. | To protect Azure Blob Storage data from unauthorized access. |

#### Control Implementation Steps

| Steps | Reference |
| ----- | --------- |
| Configure access control for Azure Blob Storage. | https://docs.microsoft.com/en-us/azure/storage/blobs/access-control-overview |

#### Control Audit Steps
| Steps |
| ----- |
| [Verify that access control is configured for Azure Blob Storage.](https://docs.microsoft.com/en-us/azure/storage/blobs/access-control-overview#verify-access-control) |
### Control Title: Monitor Azure Blob Storage for threats

| Control ID | Description | Objective |
| -- | -- | -- |
| A3 | This control ensures that Azure Blob Storage is monitored for threats. | To detect and respond to threats to Azure Blob Storage data. |

#### Control Implementation Steps

| Steps | Reference |
| ----- | --------- |
| Configure Azure Blob Storage monitoring. | https://docs.microsoft.com/en-us/azure/storage/blobs/monitoring |

#### Control Audit Steps
| Steps |
| ----- |
| [Verify that Azure Blob Storage is being monitored.](https://docs.microsoft.com/en-us/azure/storage/blobs/monitoring#verify-monitoring) |

## Azure Blob Storage Implementation Steps

| Step |
| ---- |
| [Create an Azure Blob Storage account.](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-create-account)
| [Create a blob container.](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-use-blobs-portal)
| [Upload a blob to the blob container.](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-upload-blobs)

## Azure Blob Storage Audit Steps

| Step |
| ---- |
| [Verify that the Azure Blob Storage account exists.](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-verify-account) |
| [Verify that the blob container exists.](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-verify-container) |
| [Verify that the blob exists in the blob container.](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-verify-blob) |

## References

### KPMG Internal References

- [KPMG Data Classification Standard](https://google.com)

### External References

- [NIST 800.218](https://www.google.com)

