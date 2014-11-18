vilicus - A Python network and host monitoring system
=====================================================

vilicus is a system designed to monitor and alert to problems with network
infrastructure and hosts. For example it can notify when a process is no longer
running, or monitor the CPU utilisation of a machine and alert if it is
sustained above a threshold.

It can be compared to bigger tools such as Nagios and NetXMS, but on a far
smaller scale. 

Terminology
-----------

- *check*: a check is a configured object to monitor, such as a running process or a CPU
threshold.

- *server*: the netmon server runs with a database backend and exposes an API for agents to
contact and report on configured checks.

- *agent*: an agent runs on each host to be monitored and reports back to the server with details of
its configured checks.

Architecture/design
-------------------

Each agent is completely stateless, getting most of its configuration and all
of its configured checks from the server at statup. This means its footprint is
tiny and requires only minimal dependencies.

Here is a simplified diagram of how the system works;

```

                               +--------+   4. server sends notifications if needed   +-----------------+
  /--------------------------> | server | ------------------------------------------> | email to admins |
  |                            +--------+                                             +-----------------+
  |                                |
  |                                | 1. agent contacts server and
  |                                |    and downloads list of all
  | 3. agent submits result        |    configured checks for itself
  |    of checks to server         |
  |    and "checks in",        +-------+   2. agent runs checks      +---------------------+
  |    meaning it has          | agent | <-------------------------> | is process running? |
  |    completed its checks    +-------+                             +---------------------+
  |                                |
  |                                |
  |                                |
   \-------------------------------/

```

Communication between agents and server is done via
[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) requests.
Since it uses HTTP, an agent and the server can be on the same machine, on the
same network, or across the Internet. An agent simply requires HTTP access over
port 80 to the server. A sample of the interaction between agent and server is
given below:

```
  GET /api/v1/agent/
    ^ fetch the agent object (this also verifies access)

  GET /api/v1/process_check/
    ^ get a list of this agent's process checks

  POST /api/v1/check_history/
  POST /api/v1/check_history/
  POST /api/v1/check_history/
    ^ post the results back to the server, one for each check (3 are configured)

  PUT /api/v1/agent/1/
    ^ checkout - signal to the server the agent has finished its checks for this run
```

The server never contacts any of its agents, rather each agent contacts the
server as it is assumed to be at a fixed address.

Dependencies
------------

- Server: see [requirements.txt](requirements.txt)
