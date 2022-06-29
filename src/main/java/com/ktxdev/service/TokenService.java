package com.ktxdev.service;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static com.ktxdev.utils.AutoGitConstants.*;

public class TokenService {

    public static void saveToken(String token) throws IOException {
        Path filePath = Paths.get(AUTH_PROPERTIES_FILE_PATH);

        if (!Files.exists(filePath))
            Files.createFile(filePath);

        try(OutputStream stream = new FileOutputStream(filePath.toFile())) {
            stream.write(String.format("token%s%s", TOKEN_SEPARATOR, token).getBytes(StandardCharsets.UTF_8));
        }
    }

    public static String readToken() throws IOException {
        Path authPropertiesFilePath = Paths.get(AUTH_PROPERTIES_FILE_PATH);
        try(InputStream stream = new FileInputStream(authPropertiesFilePath.toFile())) {
            String token = new String(stream.readAllBytes());
            return token.split(TOKEN_SEPARATOR)[1];
        }
    }
}
