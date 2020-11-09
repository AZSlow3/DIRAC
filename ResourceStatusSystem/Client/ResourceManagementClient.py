""" ResourceManagementClient

  Client to interact with the ResourceManagement service and from it with the DB.
"""

__RCSID__ = '$Id$'

from DIRAC.Core.Base.Client import Client, createClient


def uppercase_first_letter(key):
  """ a method that makes the first letter uppercase only (and leaves the remaining letters unaffected)
  """
  return key[0].upper() + key[1:]


@createClient('ResourceStatus/ResourceManagement')
class ResourceManagementClient(Client):
  """
  The :class:`ResourceManagementClient` class exposes the :mod:`DIRAC.ResourceManagement`
  API. All functions you need are on this client.

  You can use this client on this way

   >>> from DIRAC.ResourceManagementSystem.Client.ResourceManagementClient import ResourceManagementClient
   >>> rsClient = ResourceManagementClient()
  """

  def __init__(self, **kwargs):

    super(ResourceManagementClient, self).__init__(**kwargs)
    self.setServer('ResourceStatus/ResourceManagement')

  def _prepare(self, sendDict):

    # remove unnecessary key generated by locals()
    del sendDict['self']

    # make each key name uppercase to match database column names (case sensitive)
    for key, value in sendDict.items():
      del sendDict[key]
      if value:
        sendDict.update({uppercase_first_letter(key): value})

    return sendDict

  # AccountingCache Methods ....................................................

  def selectAccountingCache(self, name=None, plotType=None, plotName=None,
                            result=None, dateEffective=None, lastCheckTime=None, meta=None):
    '''
    Gets from PolicyResult all rows that match the parameters given.

    :param name: name of an individual of the grid topology
    :type name: string, list
    :param plotType: the plotType name (e.g. 'Pilot')
    :type plotType: string, list
    :param plotName: the plot name
    :type plotName: string, list
    :param result: command result
    :type result: string, list
    :param dateEffective: time-stamp from which the result is effective
    :type dateEffective:  datetime, list
    :param lastCheckTime: time-stamp setting last time the result was checked
    :type lastCheckTime: datetime, list
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
         For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('AccountingCache', self._prepare(locals()))

  def addOrModifyAccountingCache(self, name=None, plotType=None, plotName=None,
                                 result=None, dateEffective=None, lastCheckTime=None):
    '''
    Adds or updates-if-duplicated to AccountingCache. Using `name`, `plotType`
    and `plotName` to query the database, decides whether to insert or update the
    table.

    :param str name: name of an individual of the grid topology
    :param str plotType: name (e.g. 'Pilot')
    :param str plotName: the plot name
    :param str result: command result
    :param datetime dateEffective: timestamp from which the result is effective
    :param datetime lastCheckTime: timestamp setting last time the result was checked
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('AccountingCache', self._prepare(locals()))

  def deleteAccountingCache(self, name=None, plotType=None, plotName=None,
                            result=None, dateEffective=None, lastCheckTime=None):
    '''
    Deletes from AccountingCache all rows that match the parameters given.

    :param str name: name of an individual of the grid topology
    :param str plotType: the plotType name (e.g. 'Pilot')
    :param str plotName: the plot name
    :param str result: command result
    :param datetime dateEffective: timestamp from which the result is effective
    :param datetime lastCheckTime: timestamp setting last time the result was checked
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('AccountingCache', self._prepare(locals()))

  # GGUSTicketsCache Methods ...................................................

  def selectGGUSTicketsCache(self, gocSite=None, link=None, openTickets=None,
                             tickets=None, lastCheckTime=None, meta=None):
    '''
    Gets from GGUSTicketsCache all rows that match the parameters given.

    :param str gocSite:
    :param str link: url to the details
    :param int openTickets:
    :param str tickets:
    :param datetime lastCheckTime: timestamp setting last time the result was checked
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
       For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('GGUSTicketsCache', self._prepare(locals()))

  def deleteGGUSTicketsCache(self, gocSite=None, link=None, openTickets=None,
                             tickets=None, lastCheckTime=None):
    '''
    Deletes from GGUSTicketsCache all rows that match the parameters given.

    :param str gocSite:
    :param str link: url to the details
    :param int openTickets:
    :param str tickets:
    :param datetime lastCheckTime: timestamp setting last time the result was checked
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('GGUSTicketsCache', self._prepare(locals()))

  def addOrModifyGGUSTicketsCache(self, gocSite=None, link=None, openTickets=None,
                                  tickets=None, lastCheckTime=None):
    '''
    Adds or updates-if-duplicated to GGUSTicketsCache all rows that match the parameters given.

    :param str gocSite:
    :param str link: url to the details
    :param int openTickets:
    :param str tickets:
    :param datetime lastCheckTime: timestamp setting last time the result was checked
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('GGUSTicketsCache', self._prepare(locals()))

  # DowntimeCache Methods ......................................................

  def selectDowntimeCache(self, downtimeID=None, element=None, name=None,
                          startDate=None, endDate=None, severity=None,
                          description=None, link=None, dateEffective=None,
                          lastCheckTime=None, gOCDBServiceType=None, meta=None):
    '''
    Gets from DowntimeCache all rows that match the parameters given.

    :param downtimeID: unique id for the downtime
    :type downtimeID: string, list
    :param element: valid element in the topology (Site, Resource, Node)
    :type element: string, list
    :param name: name of the element where the downtime applies
    :type name: string, list
    :param startDate: starting time for the downtime
    :type startDate: datetime, list
    :param endDate: ending time for the downtime
    :type endDate: datetime, list
    :param severity: severity assigned by the gocdb
    :type severity: string, list
    :param description: brief description of the downtime
    :type description: string, list
    :param link: url to the details
    :type link: string, list
    :param dateEffective: time when the entry was created in this database
    :type dateEffective: datetime, list
    :param lastCheckTime: timestamp setting last time the result was checked
    :type lastCheckTime: datetime, list
    :param str gOCDBServiceType: service type assigned by gocdb
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
        For example: meta={'columns': ['Name']} will return only the 'Name' column.

    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('DowntimeCache', self._prepare(locals()))

  def deleteDowntimeCache(self, downtimeID=None, element=None, name=None,
                          startDate=None, endDate=None, severity=None,
                          description=None, link=None, dateEffective=None,
                          lastCheckTime=None, gOCDBServiceType=None):
    '''
    Deletes from DowntimeCache all rows that match the parameters given.

    :param downtimeID: unique id for the downtime
    :type downtimeID: string, list
    :param element: valid element in the topology ( Site, Resource, Node )
    :type element: string, list
    :param name: name of the element where the downtime applies
    :type name: string, list
    :param startDate: starting time for the downtime
    :type startDate: datetime, list
    :param endDate: ending time for the downtime
    :type endDate: datetime, list
    :param severity: severity assigned by the gocdb
    :type severity: string, list
    :param description: brief description of the downtime
    :type description: string, list
    :param link: url to the details
    :type link: string, list
    :param dateEffective: time when the entry was created in this database
    :type dateEffective: datetime, list
    :param lastCheckTime: time-stamp setting last time the result was checked
    :type lastCheckTime: datetime, list
    :param str gOCDBServiceType: service type assigned by gocdb
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('DowntimeCache', self._prepare(locals()))

  def addOrModifyDowntimeCache(self, downtimeID=None, element=None, name=None,
                               startDate=None, endDate=None, severity=None,
                               description=None, link=None, dateEffective=None,
                               lastCheckTime=None, gOCDBServiceType=None):
    '''
    Adds or updates-if-duplicated to DowntimeCache. Using `downtimeID` to query
    the database, decides whether to insert or update the table.

    :param str downtimeID: unique id for the downtime
    :param str element: valid element in the topology ( Site, Resource, Node )
    :param str name: name of the element where the downtime applies
    :param datetime startDate: starting time for the downtime
    :param datetime endDate: ending time for the downtime
    :param str severity: severity assigned by the gocdb
    :param str description: brief description of the downtime
    :param str link: url to the details
    :param datetime dateEffective: time when the entry was created in this database
    :param datetime lastCheckTime: timestamp setting last time the result was checked
    :param str gOCDBServiceType: service type assigned by gocdb
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('DowntimeCache', self._prepare(locals()))

  # JobCache Methods ...........................................................

  def selectJobCache(self, site=None, maskStatus=None, efficiency=None,
                     status=None, lastCheckTime=None, meta=None):
    '''
    Gets from JobCache all rows that match the parameters given.

    :param site: name of the site element
    :type site: string, list
    :param maskStatus: maskStatus for the site
    :type maskStatus: string, list
    :param efficiency: job efficiency ( successful / total )
    :type efficiency: float, list
    :param status: status for the site computed
    :type status: string, list
    :param lastCheckTime: timestamp setting last time the result was checked
    :type lastCheckTime: datetime, list
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
       For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('JobCache', self._prepare(locals()))

  def deleteJobCache(self, site=None, maskStatus=None, efficiency=None,
                     status=None, lastCheckTime=None):
    '''
    Deletes from JobCache all rows that match the parameters given.

    :param site: name of the site element
    :type site: string, list
    :param maskStatus: maskStatus for the site
    :type maskStatus: string, list
    :param efficiency: job efficiency ( successful / total )
    :type efficiency: float, list
    :param status: status for the site computed
    :type status: string, list
    :param lastCheckTime: timestamp setting last time the result was checked
    :type lastCheckTime: datetime, list
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('JobCache', self._prepare(locals()))

  def addOrModifyJobCache(self, site=None, maskStatus=None, efficiency=None,
                          status=None, lastCheckTime=None):
    '''
    Adds or updates-if-duplicated to JobCache. Using `site` to query
    the database, decides whether to insert or update the table.

    :param site: name of the site element
    :type site: string, list
    :param maskStatus: maskStatus for the site
    :type maskStatus: string, list
    :param efficiency: job efficiency ( successful / total )
    :type efficiency: float, list
    :param status: status for the site computed
    :type status: string, list
    :param lastCheckTime: time-stamp setting last time the result was checked
    :type lastCheckTime: datetime, list
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('JobCache', self._prepare(locals()))

  # TransferCache Methods ......................................................

  def selectTransferCache(self, sourceName=None, destinationName=None, metric=None,
                          value=None, lastCheckTime=None, meta=None):
    '''
    Gets from TransferCache all rows that match the parameters given.

    :param elementName: name of the element
    :type elementName: string, list
    :param direction: the element taken as Source or Destination of the transfer
    :type direction: string, list
    :param metric: measured quality of failed transfers
    :type metric: string, list
    :param value: percentage
    :type value: float, list
    :param lastCheckTime: time-stamp setting last time the result was checked
    :type lastCheckTime: float, list
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
      For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('TransferCache', self._prepare(locals()))

  def deleteTransferCache(self, sourceName=None, destinationName=None, metric=None,
                          value=None, lastCheckTime=None):
    '''
     Deletes from TransferCache all rows that match the parameters given.

    :param elementName: name of the element
    :type elementName: string, list
    :param direction: the element taken as Source or Destination of the transfer
    :type direction: string, list
    :param metric: measured quality of failed transfers
    :type metric: string, list
    :param value: percentage
    :type value: float, list
    :param lastCheckTime: time-stamp setting last time the result was checked
    :type lastCheckTime: float, list
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('TransferCache', self._prepare(locals()))

  def addOrModifyTransferCache(self, sourceName=None, destinationName=None, metric=None,
                               value=None, lastCheckTime=None):
    '''
     Adds or updates-if-duplicated to TransferCache. Using `elementName`, `direction`
     and `metric` to query the database, decides whether to insert or update the table.

    :param str elementName: name of the element
    :param str direction: the element taken as Source or Destination of the transfer
    :param str metric: measured quality of failed transfers
    :param float value: percentage
    :param datetime lastCheckTime: time-stamp setting last time the result was checked
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('TransferCache', self._prepare(locals()))

  # PilotCache Methods .........................................................

  def selectPilotCache(self, site=None, cE=None, pilotsPerJob=None,
                       pilotJobEff=None, status=None, lastCheckTime=None, meta=None):
    '''
    Gets from TransferCache all rows that match the parameters given.

    :param site: name of the site
    :type site: string, list
    :param cE: name of the CE of 'Multiple' if all site CEs are considered
    :type cE: string, list
    :param pilotsPerJob: measure calculated
    :type pilotsPerJob: float, list
    :param pilotJobEff: percentage
    :type pilotJobEff: float, list
    :param status: status of the CE / Site
    :type status: float, list
    :param lastCheckTime: measure calculated
    :type lastCheckTime: datetime, list
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
       For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('PilotCache', self._prepare(locals()))

  def deletePilotCache(self, site=None, cE=None, pilotsPerJob=None,
                       pilotJobEff=None, status=None, lastCheckTime=None):
    '''
    Deletes from TransferCache all rows that match the parameters given.

    :param site: name of the site
    :type site: string, list
    :param cE: name of the CE of 'Multiple' if all site CEs are considered
    :type cE: string, list
    :param pilotsPerJob: measure calculated
    :type pilotsPerJob: float, list
    :param pilotJobEff: percentage
    :type pilotJobEff: float, list
    :param status: status of the CE / Site
    :type status: float, list
    :param lastCheckTime: measure calculated
    :type lastCheckTime: datetime, list
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('PilotCache', self._prepare(locals()))

  def addOrModifyPilotCache(self, site=None, cE=None, pilotsPerJob=None,
                            pilotJobEff=None, status=None, lastCheckTime=None):
    '''
    Adds or updates-if-duplicated to PilotCache. Using `site` and `cE`
    to query the database, decides whether to insert or update the table.

    :param str site: name of the site
    :param str cE: name of the CE of 'Multiple' if all site CEs are considered
    :param float pilotsPerJob: measure calculated
    :param flaot pilotJobEff: percentage
    :param str status: status of the CE / Site
    :param datetime lastCheckTime: measure calculated
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('PilotCache', self._prepare(locals()))

  # PolicyResult Methods .......................................................

  def selectPolicyResult(self, element=None, name=None, policyName=None,
                         statusType=None, status=None, reason=None,
                         lastCheckTime=None, meta=None):
    '''
    Gets from PolicyResult all rows that match the parameters given.

    :param granularity: it has to be a valid element ( ValidElement ), any of the defaults:
       'Site' | 'Service' | 'Resource' | 'StorageElement'
    :type granularity: string, list
    :param name: name of the element
    :type name: string, list
    :param policyName: name of the policy
    :type policyName: string, list
    :param statusType: it has to be a valid status type for the given granularity
    :type statusType: string, list
    :param status: it has to be a valid status, any of the defaults:
        'Active' | 'Degraded' | 'Probing' | 'Banned'
    :type status: string, list
    :param reason: decision that triggered the assigned status
    :type reason: string, list
    :param lastCheckTime: time-stamp setting last time the policy result was checked
    :type lastCheckTime: datetime, list
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
        For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('PolicyResult', self._prepare(locals()))

  def deletePolicyResult(self, element=None, name=None, policyName=None,
                         statusType=None, status=None, reason=None,
                         dateEffective=None, lastCheckTime=None):
    '''
    Deletes from PolicyResult all rows that match the parameters given.

    :param granularity: it has to be a valid element ( ValidElement ), any of the defaults:
       'Site' | 'Service' | 'Resource' | 'StorageElement'
    :type granularity: string, list
    :param name: name of the element
    :type name: string, list
    :param policyName: name of the policy
    :type policyName: string, list
    :param statusType: it has to be a valid status type for the given granularity
    :type statusType: string, list
    :param status: it has to be a valid status, any of the defaults: 'Active' | 'Degraded' | 'Probing' | 'Banned'
    :type status: string, list
    :param reason: decision that triggered the assigned status
    :type reason: string, list
    :param datetime dateEffective: time-stamp from which the policy result is effective
    :param lastCheckTime: time-stamp setting last time the policy result was checked
    :type lastCheckTime: datetime, list
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('PolicyResult', self._prepare(locals()))

  def addOrModifyPolicyResult(self, element=None, name=None, policyName=None,
                              statusType=None, status=None, reason=None,
                              dateEffective=None, lastCheckTime=None):
    '''
    Adds or updates-if-duplicated to PolicyResult. Using `name`, `policyName` and
    `statusType` to query the database, decides whether to insert or update the table.

    :param str element: it has to be a valid element ( ValidElement ), any of the defaults:
       'Site' | 'Service' | 'Resource' | 'StorageElement'
    :param str name: name of the element
    :param str policyName: name of the policy
    :param str statusType: it has to be a valid status type for the given element
    :param str status: it has to be a valid status, any of the defaults:
      'Active' | 'Degraded' | 'Probing' | 'Banned'
    :param str reason: decision that triggered the assigned status
    :param datetime dateEffective: time-stamp from which the policy result is effective
    :param datetime lastCheckTime: time-stamp setting last time the policy result was checked
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('PolicyResult', self._prepare(locals()))

  # SpaceTokenOccupancyCache Methods ...........................................

  def selectSpaceTokenOccupancyCache(self, endpoint=None, token=None,
                                     total=None, guaranteed=None, free=None,
                                     lastCheckTime=None, meta=None):
    '''
    Gets from SpaceTokenOccupancyCache all rows that match the parameters given.

    :param endpoint: endpoint
    :type endpoint: string, list
    :param token: name of the token
    :type token: string, list
    :param total: total terabytes
    :type total: integer, list
    :param guaranteed: guaranteed terabytes
    :type guaranteed: integer, list
    :param free: free terabytes
    :type free: integer, list
    :param lastCheckTime: time-stamp from which the result is effective
    :type lastCheckTime: datetime, list
    :param dict meta: metadata for the mysql query. Currently it is being used only for column selection.
        For example: meta={'columns': ['Name']} will return only the 'Name' column.
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().select('SpaceTokenOccupancyCache', self._prepare(locals()))

  def deleteSpaceTokenOccupancyCache(self, endpoint=None, token=None,
                                     total=None, guaranteed=None, free=None,
                                     lastCheckTime=None):
    '''
    Deletes from SpaceTokenOccupancyCache all rows that match the parameters given.

    :param endpoint: endpoint
    :type endpoint: string, list
    :param token: name of the token
    :type token: string, list
    :param total: total terabytes
    :type total: integer, list
    :param guaranteed: guaranteed terabytes
    :type guaranteed: integer, list
    :param free: free terabytes
    :type free: integer, list
    :param lastCheckTime: time-stamp from which the result is effective
    :type lastCheckTime: datetime, list
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().delete('SpaceTokenOccupancyCache', self._prepare(locals()))

  def addOrModifySpaceTokenOccupancyCache(self, endpoint=None, token=None,
                                          total=None, guaranteed=None, free=None,
                                          lastCheckTime=None):
    '''
    Adds or updates-if-duplicated to SpaceTokenOccupancyCache. Using `site` and `token`
    to query the database, decides whether to insert or update the table.

    :param endpoint: endpoint
    :type endpoint: string, list
    :param str token: name of the token
    :param int total: total terabytes
    :param int guaranteed: guaranteed terabytes
    :param int free: free terabytes
    :param datetime lastCheckTime: time-stamp from which the result is effective
    :return: S_OK() || S_ERROR()
    '''

    return self._getRPC().addOrModify('SpaceTokenOccupancyCache',
                                      self._prepare(locals()))

# EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF
