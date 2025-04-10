@ stdcall CallNtPowerInformation (long ptr long ptr long)
@ stdcall CanUserWritePwrScheme ()
@ stdcall DeletePwrScheme (long)
@ stdcall EnumPwrSchemes (ptr long)
@ stdcall GetActivePwrScheme (ptr)
@ stdcall GetCurrentPowerPolicies (ptr ptr)
@ stdcall GetPwrCapabilities (ptr)
@ stdcall GetPwrDiskSpindownRange (ptr ptr)
@ stdcall IsAdminOverrideActive (ptr)
@ stdcall IsPwrHibernateAllowed ()
@ stdcall IsPwrShutdownAllowed ()
@ stdcall IsPwrSuspendAllowed ()
@ stdcall PowerDeterminePlatformRole ()
@ stdcall PowerDeterminePlatformRoleEx(long)
@ stdcall PowerEnumerate(long ptr ptr long long ptr ptr)
@ stdcall PowerGetActiveScheme (ptr ptr)
@ stdcall PowerSetActiveScheme (ptr ptr)
@ stdcall PowerReadACValue(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall PowerReadACValueIndex(ptr ptr ptr ptr ptr)
@ stdcall PowerReadDCValue(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall PowerReadDCValueIndex(ptr ptr ptr ptr ptr)
@ stdcall PowerReadFriendlyName (ptr ptr ptr ptr ptr ptr)
@ stdcall PowerRegisterSuspendResumeNotification(long ptr ptr)
@ stdcall PowerUnregisterSuspendResumeNotification(ptr)
@ stdcall PowerSettingRegisterNotification(ptr long ptr ptr)
@ stdcall PowerSettingUnregisterNotification(ptr)
@ stdcall PowerWriteACValueIndex(ptr ptr ptr ptr long)
@ stdcall PowerWriteDCValueIndex(ptr ptr ptr ptr long)
@ stdcall ReadGlobalPwrPolicy (ptr)
@ stdcall ReadProcessorPwrScheme (long ptr)
@ stdcall ReadPwrScheme (long ptr)
@ stdcall SetActivePwrScheme (long ptr ptr)
@ stdcall SetSuspendState (long long long)
@ stdcall WriteGlobalPwrPolicy (ptr)
@ stdcall WriteProcessorPwrScheme (long ptr)
@ stdcall WritePwrScheme (ptr str str ptr)
@ stdcall ValidatePowerPolicies (ptr ptr)
