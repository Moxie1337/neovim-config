return {
	"mg979/vim-visual-multi",
	init = function()
		vim.cmd([[
		let g:VM_leader                     = {'default': ',', 'visual': ',', 'buffer': ','}
		let g:VM_maps                       = {}
		let g:VM_custom_motions             = {'H': '0', 'L': '$'}
		let g:VM_maps['i']                  = 'm'
		let g:VM_maps['I']                  = 'M'
		let g:VM_maps['Find Under']         = '<C-m>'
		let g:VM_maps['Find Subword Under'] = '<C-m>'
		let g:VM_maps["Find Next"]          = ']'
		let g:VM_maps["Find Prev"]          = '['
		let g:VM_maps['Remove Region']      = 'q'
		let g:VM_maps['Skip Region']        = '<c-k>'
		let g:VM_maps["Undo"]               = 'l'
		let g:VM_maps["Redo"]               = '<C-r>'
		noremap <leader>sa <Plug>(VM-Select-All)
		]])
	end
}
