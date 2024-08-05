# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: anduril/taskmanager/v1/task.pub.proto, anduril/taskmanager/v1/task_manager_api.pub.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...entitymanager import v1 as __entitymanager_v1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class Status(betterproto.Enum):
    """
    The Status of a Task definition through its lifecycle. Each Definition
    Version can have its own Status. For example, Definition v1 could go
    CREATED -> SENT -> WILCO -> REPLACED, with v2 then potentially in sent
    Status.
    """

    STATUS_INVALID = 0
    STATUS_CREATED = 1
    """Initial creation Status."""

    STATUS_SCHEDULED_IN_MANAGER = 2
    """Scheduled within Task Manager to be sent at a future time."""

    STATUS_SENT = 3
    """Sent to another system (Asset), no receipt yet."""

    STATUS_MACHINE_RECEIPT = 4
    """
    In case of a human operated asset assignee, the machine was reachable and
    responded, but operator did not ACK yet.
    """

    STATUS_ACK = 5
    """
    Assignee (either human or system in case of autonomous robot) has
    acknowledged receipt of Task.
    """

    STATUS_WILCO = 6
    """Assignee confirmed they "will comply" / intend to execute Task."""

    STATUS_EXECUTING = 7
    """Task was started and is actively executing."""

    STATUS_WAITING_FOR_UPDATE = 8
    """
    Task is on hold, waiting for additional updates/information before
    proceeding.
    """

    STATUS_DONE_OK = 9
    """Task was completed successfully."""

    STATUS_DONE_NOT_OK = 10
    """
    Task has reached a terminal state but did not complete successfully, see
    error code/message.
    """

    STATUS_REPLACED = 11
    """This definition version was replaced."""

    STATUS_CANCEL_REQUESTED = 12
    """
    A Task was requested to be cancelled but not yet confirmed, will eventually
    move to DONE_NOT_OK.
    """

    STATUS_COMPLETE_REQUESTED = 13
    """
    A Task was requested to be completed successfully but not yet confirmed,
    will eventually move to DONE_NOT_OK / DONE_OK.
    """

    STATUS_VERSION_REJECTED = 14
    """
    This definition version was rejected, intended to be used when an Agent
    does not accept a new version of a task and continues using previous
    version
    """


class ErrorCode(betterproto.Enum):
    """Error code associated with a Task error."""

    ERROR_CODE_INVALID = 0
    ERROR_CODE_CANCELLED = 1
    """Task was cancelled by requester."""

    ERROR_CODE_REJECTED = 2
    """Task was rejected by assignee, see message for details."""

    ERROR_CODE_TIMEOUT = 3
    """Task Manager gave up waiting for a receipt/ack from assignee."""

    ERROR_CODE_FAILED = 4
    """Task attempted to execute, but failed."""


class EventType(betterproto.Enum):
    """The type of Task event."""

    EVENT_TYPE_INVALID = 0
    EVENT_TYPE_CREATED = 1
    """Task was created."""

    EVENT_TYPE_UPDATE = 2
    """Task was updated."""

    EVENT_TYPE_PREEXISTING = 3
    """Task already existed, but sent on a new stream connection."""


class TaskView(betterproto.Enum):
    """
    View of a Task through its lifecycle. For example, a definition v1 of a
    task may be running on an agent, indicated by TASK_VIEW_AGENT, while the
    definition v2 may not have been received yet, indicated by
    TASK_VIEW_MANAGER.
    """

    TASK_VIEW_INVALID = 0
    TASK_VIEW_MANAGER = 1
    """Represents the most recent version of the Task known to Task Manager"""

    TASK_VIEW_AGENT = 2
    """
    Represents the most recent version of the Task acknowledged or updated by
    an Agent
    """


@dataclass(eq=False, repr=False)
class Task(betterproto.Message):
    """
    A Task is something an agent can be asked to do within a battle space,
    typically against a given objective.
    """

    version: "TaskVersion" = betterproto.message_field(1)
    """Version of this Task."""

    display_name: str = betterproto.string_field(2)
    """
    Human readable display name for this Task, should be short (<100 chars).
    """

    specification: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)
    """
    Full Task parameterization, must be a message under anduril/tasks/v*/
    """

    created_by: "Principal" = betterproto.message_field(16)
    """
    Records who created this Task. This field will not change after the Task
    has been created.
    """

    last_updated_by: "Principal" = betterproto.message_field(4)
    """Records who updated this Task last."""

    last_update_time: datetime = betterproto.message_field(9)
    """Records the time of last update."""

    status: "TaskStatus" = betterproto.message_field(5)
    """The status of this Task."""

    scheduled_time: datetime = betterproto.message_field(6)
    """
    If the Task has been scheduled to execute, what time it should execute at.
    """

    relations: "Relations" = betterproto.message_field(8)
    """
    Any related Tasks associated with this, typically includes an assignee for
    this Task and/or a parent.
    """

    description: str = betterproto.string_field(10)
    """Longer, free form human readable description of this Task"""

    is_executed_elsewhere: bool = betterproto.bool_field(11)
    """
    If set, execution of this Task is managed elsewhere, not by Task Manager.
    In other words, Task manager will not attempt to update the assigned agent
    with execution instructions.
    """

    create_time: datetime = betterproto.message_field(13)
    """Time of Task creation."""

    replication: "Replication" = betterproto.message_field(14)
    """If populated, designates this to be a replicated Task."""

    initial_entities: List["TaskEntity"] = betterproto.message_field(15)
    """
    If populated, indicates an initial set of entities that can be used to
    execute an entity aware task For example, an entity Objective, an entity
    Keep In Zone, etc. These will not be updated during execution. If a
    taskable agent needs continuous updates on the entities from the COP, can
    call entity-manager, or use an AlternateId escape hatch.
    """

    owner: "Owner" = betterproto.message_field(12)
    """
    The networked owner of this Task. Populated on creation to be the asset on
    which the Task Manager is running. DO NOT UNDER ANY CIRCUMSTANCES change or
    modify this field. It is used to ensure that linear writes occur on the
    node responsible for replication of task data to other nodes running Task
    Manager.
    """


@dataclass(eq=False, repr=False)
class TaskStatus(betterproto.Message):
    """
    TaskStatus is contains information regarding the status of a Task at any
    given time. Can include related information  such as any progress towards
    Task completion, or any associated results if Task completed.
    """

    status: "Status" = betterproto.enum_field(1)
    """Status of the Task."""

    task_error: "TaskError" = betterproto.message_field(2)
    """Any errors associated with the Task."""

    progress: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(4)
    """
    Any incremental progress on the Task, should be from the tasks/v*/progress
    folder.
    """

    result: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(5)
    """Any final result of the Task, should be from tasks/v*/result folder."""

    start_time: datetime = betterproto.message_field(6)
    """
    Time the Task began execution, may not be known even for executing Tasks.
    """

    estimate: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(7)
    """
    Any estimate for how the Task will progress, should be from
    tasks/v*/estimates folder.
    """

    allocation: "Allocation" = betterproto.message_field(8)
    """Any allocated agents of the Task."""


@dataclass(eq=False, repr=False)
class TaskError(betterproto.Message):
    """
    TaskError contains an error code and message typically associated to a
    Task.
    """

    code: "ErrorCode" = betterproto.enum_field(1)
    """Error code for Task error."""

    message: str = betterproto.string_field(2)
    """Descriptive human-readable string regarding this error."""


@dataclass(eq=False, repr=False)
class Principal(betterproto.Message):
    """A Principal is an entity that has authority over this Task."""

    system: "System" = betterproto.message_field(1, group="agent")
    user: "User" = betterproto.message_field(2, group="agent")
    team: "Team" = betterproto.message_field(4, group="agent")
    on_behalf_of: "Principal" = betterproto.message_field(3)
    """
    The Principal _this_ Principal is acting on behalf of. For example, if
    there is a Flux node connected to a non-Flux node, and that Flux node wants
    to act "on behalf of" that non-Flux node, _this_ Principal would represent
    the Flux node, and this "on_behalf_of" Principal would represent the non-
    Flux node. Likely only populated once in the nesting (i.e. the
    "on_behalf_of" Principal would not have another "on_behalf_of" in most
    cases).
    """


@dataclass(eq=False, repr=False)
class System(betterproto.Message):
    """System Principal representing some autonomous system."""

    service_name: str = betterproto.string_field(1)
    """Name of the service associated with this System."""

    entity_id: str = betterproto.string_field(2)
    """The Entity ID of the System."""

    asset_id: str = betterproto.string_field(3)
    """The Asset ID of the System."""

    manages_own_scheduling: bool = betterproto.bool_field(4)
    """
    Whether the System Principal (for example, an Asset) can own scheduling.
    This means we bypass manager-owned scheduling and defer to the system
    Principal to handle scheduling and give us status updates for the Task.
    Regardless of the value defined by the client, the Task Manager will
    determine and set this value appropriately.
    """


@dataclass(eq=False, repr=False)
class User(betterproto.Message):
    """A User Principal representing a human."""

    user_id: str = betterproto.string_field(1)
    """The User ID associated with this User."""


@dataclass(eq=False, repr=False)
class Relations(betterproto.Message):
    """
    Relations describes the relationships of this Task, such as assignment, or
    if the Task has any parents.
    """

    assignee: "Principal" = betterproto.message_field(1)
    """Who or what, if anyone, this Task is currently assigned to."""

    parent_task_id: str = betterproto.string_field(2)
    """If this Task is a "sub-Task", what is its parent, none if empty."""


@dataclass(eq=False, repr=False)
class TaskEvent(betterproto.Message):
    """Holds Tasks and its associated Events, e.g. CREATED."""

    event_type: "EventType" = betterproto.enum_field(1)
    """Type of Event."""

    task: "Task" = betterproto.message_field(2)
    """Task associated with this TaskEvent."""

    task_view: "TaskView" = betterproto.enum_field(3)
    """View associated with this task."""

    time: datetime = betterproto.message_field(4)
    """===== Time Series Updates ===== Timestamp for time-series to index."""


@dataclass(eq=False, repr=False)
class TaskVersion(betterproto.Message):
    """Version of a Task."""

    task_id: str = betterproto.string_field(1)
    """The unique ID for this Task."""

    definition_version: int = betterproto.uint32_field(2)
    """
    Increments on definition (i.e. not TaskStatus) change. 0 is unset, starts
    at 1 on creation.
    """

    status_version: int = betterproto.uint32_field(3)
    """
    Increments on changes to TaskStatus. 0 is unset, starts at 1 on creation.
    """


@dataclass(eq=False, repr=False)
class StatusUpdate(betterproto.Message):
    """a Task status update that could come in via RPC or Flux."""

    version: "TaskVersion" = betterproto.message_field(1)
    """Version of the Task."""

    status: "TaskStatus" = betterproto.message_field(2)
    """Status of the Task."""

    author: "Principal" = betterproto.message_field(3)
    """
    Author of the StatusUpdate message. Used to set the LastUpdatedBy field of
    the Task.
    """

    scheduled_time: datetime = betterproto.message_field(4)
    """
    Typically provided if a user is manually managing a Task, or if an asset
    owns scheduling.
    """


@dataclass(eq=False, repr=False)
class DefinitionUpdate(betterproto.Message):
    """Flux message representing a Task create or update."""

    task: "Task" = betterproto.message_field(1)
    """
    New task definition being created or updated. The last_updated_by and
    specification fields inside the task object must be defined. Definition
    version must also be incremented by the publisher on updates. We do not
    look at the fields create_time or last_update_time in this object, they are
    instead set by task-manager.
    """


@dataclass(eq=False, repr=False)
class Owner(betterproto.Message):
    """
    Owner designates the networked flux node responsible for linear writes of a
    Task data.
    """

    asset_id: str = betterproto.string_field(1)
    """Flux Asset ID of the owner."""

    entity_id: str = betterproto.string_field(2)
    """Entity ID of the owner."""


@dataclass(eq=False, repr=False)
class Replication(betterproto.Message):
    """Any metadata associated with the replication of a Task."""

    stale_time: datetime = betterproto.message_field(1)
    """Time by which this Task should be assumed to be stale."""


@dataclass(eq=False, repr=False)
class Allocation(betterproto.Message):
    """Allocation contains a list of agents allocated to a Task."""

    active_agents: List["Agent"] = betterproto.message_field(1)
    """Agents actively being utilized in a Task."""


@dataclass(eq=False, repr=False)
class Team(betterproto.Message):
    """Represents a team of agents"""

    entity_id: str = betterproto.string_field(1)
    """Entity ID of the team"""

    members: List["Agent"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Agent(betterproto.Message):
    """Represents an Agent on the Battlespace."""

    asset_id: str = betterproto.string_field(1)
    """Asset ID of the agent."""

    entity_id: str = betterproto.string_field(2)
    """Entity ID of the agent."""


@dataclass(eq=False, repr=False)
class TaskEntity(betterproto.Message):
    """
    Wrapper of an entity passed in Tasking, used to hold an additional
    information, and as a future extension point.
    """

    entity: "__entitymanager_v1__.Entity" = betterproto.message_field(1)
    """The wrapped entity-manager entity."""

    snapshot: bool = betterproto.bool_field(2)
    """
    Indicates that this entity was generated from a snapshot of a live entity.
    """


@dataclass(eq=False, repr=False)
class CreateTaskRequest(betterproto.Message):
    """Request to create a Task."""

    display_name: str = betterproto.string_field(1)
    """
    Human readable display name for this Task, should be short (<100 chars).
    """

    specification: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    """
    Full task parameterization, must be a message under anduril/tasks/v*/.
    """

    author: "Principal" = betterproto.message_field(3)
    """
    Who or what is creating this Task. For example, if a user created this Task
    via a UI, it would  contain the "user" Principal type with the user ID of
    that user. Or if a service is calling the  CreateTask endpoint, then a
    "service" Principal type is to be provided.
    """

    relations: "Relations" = betterproto.message_field(5)
    """
    Any relationships associated with this Task, such as a parent Task or an
    assignee this Task is designated to  for execution.
    """

    description: str = betterproto.string_field(6)
    """Longer, free form human readable description of this Task."""

    is_executed_elsewhere: bool = betterproto.bool_field(7)
    """
    If set, then task-manager will not trigger execution of this task on an
    agent. Useful for when ingesting tasks from an external system that is
    triggering execution of tasks on agents.
    """

    task_id: str = betterproto.string_field(8)
    """
    If non-empty, will set the requested Task ID, otherwise will generate a new
    random GUID.  Will reject if supplied Task ID does not match
    `[A-Za-z0-9_-.]{5,36}`.
    """

    initial_entities: List["TaskEntity"] = betterproto.message_field(9)
    """
    Indicates an initial set of entities that can be used to execute an entity
    aware task. For example, an entity Objective, an entity Keep In Zone, etc.
    """


@dataclass(eq=False, repr=False)
class CreateTaskResponse(betterproto.Message):
    """Response to a Create Task request."""

    task: "Task" = betterproto.message_field(1)
    """Task that was created."""


@dataclass(eq=False, repr=False)
class GetTaskRequest(betterproto.Message):
    """Request to get a Task."""

    task_id: str = betterproto.string_field(1)
    """ID of Task to get."""

    definition_version: int = betterproto.uint32_field(2)
    """
    Optional - if > 0, will get specific definition_version, otherwise latest
    (highest) definition_version is used.
    """

    task_view: "TaskView" = betterproto.enum_field(3)
    """
    Optional - select which view of the task to fetch. If not set, defaults to
    TASK_VIEW_MANAGER.
    """


@dataclass(eq=False, repr=False)
class GetTaskResponse(betterproto.Message):
    """Response to a Get Task request."""

    task: "Task" = betterproto.message_field(1)
    """Task that received."""


@dataclass(eq=False, repr=False)
class UpdateTaskRequest(betterproto.Message):
    """Request to update a Task."""

    task: "Task" = betterproto.message_field(1)
    """New Task definition."""

    is_executed_elsewhere: bool = betterproto.bool_field(7)
    """
    If set, execution of this Task is managed elsewhere, not by task-manager.
    In other words, Task Manager will not attempt to update the assigned agent
    with execution instructions. We note that this will also override the
    existing is_executed_elsewhere value in the Task object provided in this
    request.
    """


@dataclass(eq=False, repr=False)
class UpdateTaskResponse(betterproto.Message):
    """Response to an Update Task request."""

    task: "Task" = betterproto.message_field(1)
    """the updated task"""


@dataclass(eq=False, repr=False)
class UpdateStatusRequest(betterproto.Message):
    """Request to update a Task's status."""

    status_update: "StatusUpdate" = betterproto.message_field(1)
    """The updated status."""


@dataclass(eq=False, repr=False)
class UpdateStatusResponse(betterproto.Message):
    """Response to an Update Status request."""

    task: "Task" = betterproto.message_field(1)
    """The updated Task."""


@dataclass(eq=False, repr=False)
class StreamTasksRequest(betterproto.Message):
    """
    Request to Stream Tasks. Returns all live Tasks (aka all not-DONE Tasks).
    """

    rate_limit: "RateLimit" = betterproto.message_field(1)
    """Optional rate limiting on StreamTasksResponses."""

    views: List["TaskView"] = betterproto.enum_field(2)
    """
    Optional additional views of a Task. If not set, defaults to
    TASK_VIEW_MANAGER.
    """

    heartbeat_period_millis: int = betterproto.uint32_field(3)
    """
    Optional period (in milliseconds) at which a Heartbeat message will be sent
    on the message stream. If this field is unset then no Heartbeat messages
    are sent.
    """


@dataclass(eq=False, repr=False)
class StreamTasksResponse(betterproto.Message):
    """
    Response stream will be fed all matching pre-existing live Tasks, plus any
    new events ongoing.
    """

    task_event: "TaskEvent" = betterproto.message_field(1)
    """Task event associated with the streaming request."""

    heartbeat: "Heartbeat" = betterproto.message_field(2)
    """Heartbeat message signaling liveliness of the stream."""


@dataclass(eq=False, repr=False)
class RateLimit(betterproto.Message):
    """Rate limiting / down-sampling parameters."""

    update_per_task_limit_ms: int = betterproto.uint32_field(1)
    """
    Specifies a minimum duration in milliseconds after an update for a given
    task before another one will be sent for the same task. A value of 0 is
    treated as unset. If set, value must be >= 250. Example: if set to 1000,
    and 4 events occur (ms since start) at T0, T500, T900, T2100, then event
    from T0 will be sent at T0, T500 will be dropped, T900 will be sent at
    minimum of T1000, and T2100 will be sent on time (2100) This will only
    limit updates, other events will be sent immediately, with a delete
    clearing anything held
    """


@dataclass(eq=False, repr=False)
class Heartbeat(betterproto.Message):
    timestamp: datetime = betterproto.message_field(1)
    """The time at which the Heartbeat was sent."""


class TaskManagerApiStub(betterproto.ServiceStub):
    async def create_task(
        self,
        create_task_request: "CreateTaskRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "CreateTaskResponse":
        return await self._unary_unary(
            "/anduril.taskmanager.v1.TaskManagerAPI/CreateTask",
            create_task_request,
            CreateTaskResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_task(
        self,
        get_task_request: "GetTaskRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GetTaskResponse":
        return await self._unary_unary(
            "/anduril.taskmanager.v1.TaskManagerAPI/GetTask",
            get_task_request,
            GetTaskResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_task(
        self,
        update_task_request: "UpdateTaskRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UpdateTaskResponse":
        return await self._unary_unary(
            "/anduril.taskmanager.v1.TaskManagerAPI/UpdateTask",
            update_task_request,
            UpdateTaskResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_status(
        self,
        update_status_request: "UpdateStatusRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UpdateStatusResponse":
        return await self._unary_unary(
            "/anduril.taskmanager.v1.TaskManagerAPI/UpdateStatus",
            update_status_request,
            UpdateStatusResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def stream_tasks(
        self,
        stream_tasks_request: "StreamTasksRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["StreamTasksResponse"]:
        async for response in self._unary_stream(
            "/anduril.taskmanager.v1.TaskManagerAPI/StreamTasks",
            stream_tasks_request,
            StreamTasksResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class TaskManagerApiBase(ServiceBase):

    async def create_task(
        self, create_task_request: "CreateTaskRequest"
    ) -> "CreateTaskResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_task(self, get_task_request: "GetTaskRequest") -> "GetTaskResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_task(
        self, update_task_request: "UpdateTaskRequest"
    ) -> "UpdateTaskResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_status(
        self, update_status_request: "UpdateStatusRequest"
    ) -> "UpdateStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def stream_tasks(
        self, stream_tasks_request: "StreamTasksRequest"
    ) -> AsyncIterator["StreamTasksResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
        yield StreamTasksResponse()

    async def __rpc_create_task(
        self, stream: "grpclib.server.Stream[CreateTaskRequest, CreateTaskResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_task(request)
        await stream.send_message(response)

    async def __rpc_get_task(
        self, stream: "grpclib.server.Stream[GetTaskRequest, GetTaskResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_task(request)
        await stream.send_message(response)

    async def __rpc_update_task(
        self, stream: "grpclib.server.Stream[UpdateTaskRequest, UpdateTaskResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_task(request)
        await stream.send_message(response)

    async def __rpc_update_status(
        self, stream: "grpclib.server.Stream[UpdateStatusRequest, UpdateStatusResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_status(request)
        await stream.send_message(response)

    async def __rpc_stream_tasks(
        self, stream: "grpclib.server.Stream[StreamTasksRequest, StreamTasksResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.stream_tasks,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/anduril.taskmanager.v1.TaskManagerAPI/CreateTask": grpclib.const.Handler(
                self.__rpc_create_task,
                grpclib.const.Cardinality.UNARY_UNARY,
                CreateTaskRequest,
                CreateTaskResponse,
            ),
            "/anduril.taskmanager.v1.TaskManagerAPI/GetTask": grpclib.const.Handler(
                self.__rpc_get_task,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetTaskRequest,
                GetTaskResponse,
            ),
            "/anduril.taskmanager.v1.TaskManagerAPI/UpdateTask": grpclib.const.Handler(
                self.__rpc_update_task,
                grpclib.const.Cardinality.UNARY_UNARY,
                UpdateTaskRequest,
                UpdateTaskResponse,
            ),
            "/anduril.taskmanager.v1.TaskManagerAPI/UpdateStatus": grpclib.const.Handler(
                self.__rpc_update_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                UpdateStatusRequest,
                UpdateStatusResponse,
            ),
            "/anduril.taskmanager.v1.TaskManagerAPI/StreamTasks": grpclib.const.Handler(
                self.__rpc_stream_tasks,
                grpclib.const.Cardinality.UNARY_STREAM,
                StreamTasksRequest,
                StreamTasksResponse,
            ),
        }
