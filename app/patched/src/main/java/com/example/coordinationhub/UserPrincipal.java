package com.example.coordinationhub;

import java.util.Set;

public class UserPrincipal {
    private final Set<String> roles;
    private final boolean mfaAuthenticated;

    public UserPrincipal(Set<String> roles, boolean mfaAuthenticated) {
        this.roles = roles;
        this.mfaAuthenticated = mfaAuthenticated;
    }

    public boolean hasRole(String role) {
        return roles != null && roles.contains(role);
    }

    public boolean isMfaAuthenticated() {
        return mfaAuthenticated;
    }
}

