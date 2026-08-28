package com.example.coordinationhub;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class MessageController {
    private final Connection connection;

    public MessageController(Connection connection) {
        this.connection = connection;
    }

    public String getMessageById(String messageId) throws Exception {
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(
                "SELECT body FROM messages WHERE id = '" + messageId + "'");
        return resultSet.next() ? resultSet.getString("body") : "";
    }

    public String renderMessage(String author, String body) {
        return "<div class='message'><b>" + author + "</b><p>" + body + "</p></div>";
    }

    public boolean isAdmin(String roleHeader) {
        return "admin".equals(roleHeader);
    }
}

