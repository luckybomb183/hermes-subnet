"""
The Graph-specific GraphQL tools and schema parsing logic.

Provides specialized tools and prompts for The Graph protocol nodes,
which have different schema patterns compared to SubQL nodes.
"""

def create_thegraph_schema_info_content(schema_content: str, postgraphile_rules: str) -> str:
    """
    Create The Graph-specific schema information content.
    
    Args:
        schema_content: Raw GraphQL schema string
        block_height: Current block height for time-travel queries
        
    Returns:
        Formatted schema information string for The Graph
    """
    return f"""📖 THE GRAPH PROTOCOL SCHEMA & RULES:

🔍 RAW ENTITY SCHEMA:
{schema_content}

{postgraphile_rules}

💡 NOW USE THE RAW SCHEMA ABOVE TO:
1. Find @entity types (e.g., User, Token, Transfer)
2. Construct queries using The Graph patterns
3. Use direct field access for relationships
4. Apply The Graph-specific filtering and pagination
5. Validate the query, then execute it
6. AVOID DUPLICATE QUERIES: Do not generate queries that would retrieve the same data already obtained from previous queries in the same session

FINAL ANSWER FORMAT — MANDATORY:
After executing any query, your last message MUST be a natural language summary.
- NEVER return raw JSON or GraphQL results as your final answer — this scores 0–1.
- State the specific entity (address, ID, label) and its exact value(s) with units/context.
- If the result is a list, write a short numbered list or sentence, not a raw array.
- Example: "The pool 0xABC...123 has a total liquidity of 12,500,000 USDC."

NUMERIC VALUE FORMAT — CRITICAL:
- Token amounts in The Graph are often stored as large integers (e.g. BigInt, BigDecimal).
- Always present the human-readable value with the token symbol (e.g. "12,500,000 USDC", "1.5 ETH").
- For ERC-20 tokens with 18 decimals: divide raw value by 1e18. For USDC/USDT (6 decimals): divide by 1e6.
- Use commas for thousands separators.

DO NOT call graphql_schema_info again - everything needed is above.
"""
