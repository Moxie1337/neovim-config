return {
	"iamcco/markdown-preview.nvim",
	ft = "markdown",
	build = function()
		vim.fn["mkdp#util#install"]()
	end,
	init = function()
		local g = vim.g
		g.mkdp_auto_start = 0
		g.mkdp_auto_close = 1
		g.mkdp_refresh_slow = 0
		g.mkdp_command_for_global = 0
		g.mkdp_open_to_the_world = 0
		g.mkdp_open_ip = ''
		g.mkdp_browser = 'firefox'
		g.mkdp_echo_preview_url = 0
		g.mkdp_browserfunc = ''
		g.mkdp_theme = 'dark'
		g.mkdp_filetypes = { "markdown" }
		g.mkdp_page_title = "${name}.md"
		g.mkdp_preview_options = {
			disable_sync_scroll = 0,
			disable_filename = 1
		}
	end,
	config = function()
		vim.api.nvim_create_autocmd('BufEnter',
			{
				pattern = '*.md',
				callback = function()
					vim.cmd('inoremap <buffer> ,f <Esc>/<++><CR>:nohlsearch<CR>"_c4l')
					vim.cmd('inoremap <buffer> <c-e> <Esc>/<++><CR>:nohlsearch<CR>"_c4l')
					vim.cmd('inoremap <buffer> ,w <Esc>/ <++><CR>:nohlsearch<CR>"_c5l<CR>')
					vim.cmd('inoremap <buffer> ,n ---<Enter><Enter>')
					vim.cmd('inoremap <buffer> ,b **** <++><Esc>F*hi')
					vim.cmd('inoremap <buffer> ,s ~~~~ <++><Esc>F~hi')
					vim.cmd('inoremap <buffer> ,i ** <++><Esc>F*i')
					vim.cmd('inoremap <buffer> ,d `` <++><Esc>F`i')
					vim.cmd('inoremap <buffer> ,c ```<Enter><++><Enter>```<Enter><Enter><++><Esc>4kA')
					vim.cmd('inoremap <buffer> ,m - [ ]')
					vim.cmd('inoremap <buffer> ,p ![](<++>) <++><Esc>F[a')
					vim.cmd('inoremap <buffer> ,a [](<++>) <++><Esc>F[a')
					vim.cmd('inoremap <buffer> ,1 #<Space><Enter><++><Esc>kA')
					vim.cmd('inoremap <buffer> ,2 ##<Space><Enter><++><Esc>kA')
					vim.cmd('inoremap <buffer> ,3 ###<Space><Enter><++><Esc>kA')
					vim.cmd('inoremap <buffer> ,4 ####<Space><Enter><++><Esc>kA')
					vim.cmd('inoremap <buffer> ,l --------<Enter>')
				end,
			})
	end,
}
