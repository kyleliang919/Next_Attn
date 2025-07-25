from fsq import FSQ

class FSQAttention(nn.Module):
    def __init__(self, levels = [8,5,5,5], dropout=0.0, causal=False):
        super().__init__()
        self.quantizer = FSQ(levels)
        self.dropout = dropout
        self.causal = causal

    def forward(self, q, k, v, attn_mask=None):
        # Apply quantization to K and V
        k_q, k_indice = self.quantizer(k)
        v_q, v_indice = self.quantizer(v)

        # Use torch's built-in attention
        return F.scaled_dot_product_attention(
            q, k_q, v_q, attn_mask=attn_mask,
            dropout_p=self.dropout,
            is_causal=self.causal
        ), (k_indice, v_indice)
