# Evidence index

The owner supplied these artifacts for the router investigation. Four distinct images are included; the PCB photograph was attached twice and is stored once. Images are reproduced unchanged. The owner explicitly requested that the PCB photo retain its labels.

| Artifact | Evidence type | What it supports |
| --- | --- | --- |
| [PCB overview](images/pcb-overview.jpeg) | Owner-supplied photograph | HG323RW_V3.6 silkscreen, physical layout, labeled console pads; no voltage measurement |
| [CLI command table](images/cli-command-table.png) | Owner-supplied Ghidra screenshot | Shell help/command string pointers; visible matching routine |
| [CLI string references](images/cli-string-xrefs.png) | Owner-supplied Ghidra screenshot | Two data references to the shell help string |
| [Startup shell symbol](images/startup-shell-symbol.png) | Owner-supplied Ghidra screenshot | PW_CMD_SHELL and PW_HOME_DIR references; partial decompiler view |
| [Boot excerpts](boot-excerpts.txt) | Selected original log lines | Bootloader, RAM/flash/clocks, kernel, console, filesystem, BusyBox, and logged SSH filtering commands |
| [Offline validation](offline-validation.md) | Checks performed on supplied files | Complete hex-to-image reconstruction, regular-file extraction, CLI equality and ELF address mapping |
| [Firmware manifest](firmware-manifest.json) | Artifact sizes and SHA-256 digests | Exact identity of locally inspected files |
| [Conversion script](../tools/hex_to_bin.py) | Unmodified owner-provided script | Reconstruction of this specific md.b-style capture |
| [Account metadata](account-metadata.txt) | Redacted conversation transcription | UID/GID/home/login program |
| [Original Dropbear report](dropbear-report.txt) | Historical user statement | Original report; now supplemented by binary inspection |

## Provenance and limits

The three Ghidra PNGs arrived with filenames beginning “ChatGPT Image”. They are treated as owner-supplied visual evidence, not authenticated original captures. The CLI string addresses were independently checked against the supplied binary. No claim is made that the images prove a complete shell-launch call chain.

Boot excerpts retain original line numbers and redact the build-host identifier. Omitted lines were not published. Historical firewall commands in the log must not be mistaken for commands to run.

The raw firmware and full extracted tree remain local analysis inputs. This repository does not redistribute the firmware or embedded SSH private key. Factory defaults do not establish that every embedded artifact is appropriate or necessary to redistribute.

Root identity and successful SSH login remain reported/unverified respectively. No live router session was performed during documentation.
