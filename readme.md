problem:

something broke on your windows install , so you make a backup of ur drive and reinstall windows
not u need to copy over all the programs/program config, windows configuration and customization

solution:

program that scans the source (drive/folder/image file) for stuff to move over

- [x] Programs
- [ ] %userprofile% (includes user registry)
      (copying userprofile includes registry and dektop icons and taskbar icons)
  - [ ] registry entires both related to programs like putty sessions and windows configuration like file explorer right click
    - [ ] environment variables
  - [ ] desktop icons
    - [ ] desktop icon registry bag
  - [ ] taskbar icons
  - [ ] taskbar icon configuration (like which tray icons shouldnt be folded)

exclusions (files that can't/shouldn't be copied over):

- \ProgramData\Microsoft\Windows Defender Advanced Threat Protection
- \Program Files\Windows Defender Advanced Threat Protection
