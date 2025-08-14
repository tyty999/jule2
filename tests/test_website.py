from playwright.sync_api import Page, expect
import os

def get_file_url(file_name):
    """
    Returns the absolute file URL for a given file name.
    """
    return f"file://{os.path.abspath(file_name)}"

def test_home_page(page: Page):
    """
    Tests that the home page loads correctly.
    """
    page.goto(get_file_url("index.html"))
    expect(page).to_have_title("Modern Generative AI Agents Development")

def test_introduction_page(page: Page):
    """
    Tests that the introduction page loads correctly.
    """
    page.goto(get_file_url("introduction.html"))
    expect(page).to_have_title("Introduction to Generative AI Agents")

def test_multi_agent_page(page: Page):
    """
    Tests that the multi-agent page loads correctly.
    """
    page.goto(get_file_url("multi_agent.html"))
    expect(page).to_have_title("Multi-Agent Systems")

def test_mcp_page(page: Page):
    """
    Tests that the MCP page loads correctly.
    """
    page.goto(get_file_url("mcp.html"))
    expect(page).to_have_title("Model-Context Protocol (MCP)")

def test_a2a_page(page: Page):
    """
    Tests that the A2A page loads correctly.
    """
    page.goto(get_file_url("a2a.html"))
    expect(page).to_have_title("Agent-to-Agent (A2A) Communication")

def test_adk_page(page: Page):
    """
    Tests that the ADK page loads correctly.
    """
    page.goto(get_file_url("adk.html"))
    expect(page).to_have_title("ADK SDK from Google")

def test_project_page(page: Page):
    """
    Tests that the final project page loads correctly.
    """
    page.goto(get_file_url("project.html"))
    expect(page).to_have_title("Final Project")
