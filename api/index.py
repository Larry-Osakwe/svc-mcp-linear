"""Vercel serverless function entry point."""

from src.server import mcp

app = mcp.http_app(path="/mcp")
