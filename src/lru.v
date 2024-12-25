module lru (
    input wire clk,
    input wire rst_n,
    input wire read,
    input wire write,
    input wire [2:0] addr,
    input wire [7:0] in,
    output reg [7:0] out
);
    reg [7:0] mem [7:0];
    reg [7:0] sel [7:0];

    reg [3:0] i;
    reg [7:0] min_value;
    reg [2:0] min_index;
    always @(negedge clk) begin
        if (!rst_n) begin
            for (i = 0; i < 8; i = i + 1) begin
                mem[i] <= 8'b0;
                sel[i] <= 8'b0;
            end
            min_index <= 0;
            min_value <= 0;
        end else if (read) begin
            out = mem[addr];
            sel[addr] = 8'b11111111;
            for (i = 0; i < 8; i = i + 1) begin
                sel[i][7 - addr] = 0;
            end
        end else if (write) begin
            min_value = sel[0];
            min_index = 0;
            for (i = 1; i < 8; i = i + 1) begin
                if (sel[i] < min_value) begin
                    min_value = sel[i];
                    min_index = i;
                end
            end
            mem[min_index] = in;

            sel[min_index] = 8'b11111111;
            for (i = 0; i < 8; i = i + 1) begin
                sel[i][7 - min_index] = 0;
            end
        end
    end
endmodule
