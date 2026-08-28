package com.example.coordinationhub;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import org.owasp.encoder.Encode;

public class MessageController {
    private final Connection connection;

    public MessageController(Connection connection) {
        this.connection = connection;
    }

    public String getMessageById(String messageId) throws Exception {
        String query = "SELECT body FROM messages WHERE id = ?";
        PreparedStatement statement = connection.prepareStatement(query);
        statement.setString(1, messageId);
        ResultSet resultSet = statement.executeQuery();
        return resultSet.next() ? resultSet.getString("body") : "";
    }

    public String renderMessage(String author, String body) {
        return "<div class='message'><b>"
                + Encode.forHtml(author)
                + "</b><p>"
                + Encode.forHtml(body)
                + "</p></div>";
    }

    public boolean isAdmin(UserPrincipal user) {
        return user != null && user.hasRole("ADMIN") && user.isMfaAuthenticated();
    }
}

