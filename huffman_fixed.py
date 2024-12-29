global str, char_binary_mapping
str = "ABBCCCCGGGGDEAAAEDBBBDFAGG"

class HuffmanNode:
    def _init_(self, freq, data, left, right):
        self.char = data
        self.freq = freq
        self.left = left
        self.right = right

    def _repr_(self) -> str:
        return f"({self.char},{self.freq})"

def Generate_tree(mapping):
    keyset = mapping.keys()
    pq = []
    for c in keyset:
        node = HuffmanNode(mapping[c], c, None, None)
        pq.append(node)

    pd = sorted(pq, key=lambda x: x.freq)
    print(pd)

    while len(pd) > 1:
        left = pd.pop(0)
        right = pd.pop(0)
        merged_Node = HuffmanNode(left.freq + right.freq, "_", left, right)
        pd.append(merged_Node)

        pd = sorted(pd, key=lambda x: x.freq)
        print(pd)

    return pd

def encode_frequencies(string):
    mapping = {}
    for c in string:
        if c in mapping:
            mapping[c] += 1
        else:
            mapping[c] = 1
    return mapping

def set_binary_code(node, code_str):
    if node is not None:
        if node.left is None and node.right is None:
            char_binary_mapping[node.char] = code_str
            print(node.char, code_str)
            return
        set_binary_code(node.left, code_str + "0")
        set_binary_code(node.right, code_str + "1")

def encode_string(string):
    binary_encoded = ""
    for c in string:
        binary_encoded += char_binary_mapping[c]
    return binary_encoded

def decode_string(binary_str, root):
    decoded_str = ""
    current_node = root
    for bit in binary_str:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.left is None and current_node.right is None:
            decoded_str += current_node.char
            current_node = root
    return decoded_str

# Main Execution
print("Character Frequencies:")
char_binary_mapping = {}
root = Generate_tree(encode_frequencies(str))
set_binary_code(root[0], "")

print("\nHuffman Encoding Table:")
print(char_binary_mapping)

binary_encoded_str = encode_string(str)
print("\nEncoded String:")
print(binary_encoded_str)

decoded_str = decode_string(binary_encoded_str, root[0])
print("\nDecoded String:")
print(decoded_str)