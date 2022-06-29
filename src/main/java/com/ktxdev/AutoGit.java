package com.ktxdev;

import com.ktxdev.exceptions.InvalidArgsException;
import com.ktxdev.service.TokenService;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static com.ktxdev.utils.AutoGitConstants.*;

public class AutoGit {
    public static void main(String[] args) throws IOException {
        String command = args[0].split("=")[0];

        switch (command) {
            case CONFIG_TOKEN_COMMAND:
                String[] t = args[0].split("=");

                if (t.length == 2) {
                    TokenService.saveToken(t[1]);
                    System.out.println("Token added successfully!");
                } else {
                    String token = TokenService.readToken();
                    System.out.println(token);
                }
                break;
            case CREATE_COMMAND:
                System.out.println(args[0]);
                if (args.length % 2 != 0) {
                    throw new InvalidArgsException("Some arguments are missing");
                }
                break;
            default:
                throw new InvalidArgsException(String.format("No action matched for command: %s", command));
        }
    }
}