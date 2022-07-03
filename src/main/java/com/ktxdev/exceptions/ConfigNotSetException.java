package com.ktxdev.exceptions;

public class ConfigNotSetException extends RuntimeException {
    public ConfigNotSetException(String message) {
        super(message);
    }
}
